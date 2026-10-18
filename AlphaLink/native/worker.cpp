// Original AlphaLink adapter. Build against the user's Sony Camera Remote SDK 2.02.
#include "CameraRemote_SDK.h"
#include "IDeviceCallback.h"
#include <cstring>
#include <algorithm>
#include <chrono>
#include <condition_variable>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <mutex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
namespace sdk = SCRSDK;
using namespace std::chrono_literals;
namespace fs = std::filesystem;

std::string quote(const std::string& s) {
    std::ostringstream o; o << '"';
    for (unsigned char c : s) {
        if (c == '"' || c == '\\') o << '\\' << c;
        else if (c < 32) o << "\\u" << std::hex << std::setw(4) << std::setfill('0') << (int)c;
        else o << c;
    }
    return o.str() + '"';
}
std::string unhex(const std::string& s) {
    if (s == "-") return {};
    if (s.size() % 2) throw std::runtime_error("Malformed protocol string");
    std::string out;
    auto digit=[](char c)->int { if(c>='0'&&c<='9')return c-'0'; if(c>='a'&&c<='f')return c-'a'+10; throw std::runtime_error("Malformed hex"); };
    for (size_t i=0;i<s.size();i+=2) out += static_cast<char>(digit(s[i])*16+digit(s[i+1]));
    if (out.find('\0') != std::string::npos) throw std::runtime_error("Embedded NUL rejected");
    return out;
}
void emit(const std::string& json) { std::cout << "@alphalink " << json << std::endl; }
void check(sdk::CrError e, const char* operation) {
    if (e != sdk::CrError_None) { std::ostringstream o; o << operation << " failed (Sony SDK 0x" << std::hex << e << "). Check camera mode, firmware, pairing and authentication."; throw std::runtime_error(o.str()); }
}

class Camera final : public sdk::IDeviceCallback {
    std::mutex mu;
    std::condition_variable cv;
    bool connected=false, disconnected=true, terminal=false, transferring=false, transferDone=false;
    CrInt32u error=0;
    sdk::CrContentHandle active=0;
    sdk::CrDeviceHandle device=0;
    sdk::ICrEnumCameraObjectInfo* enumeration=nullptr;
    sdk::ICrCameraObjectInfo* info=nullptr;
    std::string fingerprint, user, password;
public:
    void OnConnected(sdk::DeviceConnectionVersioin) override {
        std::lock_guard<std::mutex> lock(mu); connected=true; disconnected=false; terminal=false; cv.notify_all();
    }
    void OnDisconnected(CrInt32u e) override {
        std::lock_guard<std::mutex> lock(mu); connected=false; disconnected=true; terminal=true; error=e; cv.notify_all();
    }
    void OnError(CrInt32u e) override {
        std::lock_guard<std::mutex> lock(mu); error=e; terminal=true; cv.notify_all();
    }
    void OnNotifyContentsTransfer(CrInt32u n, sdk::CrContentHandle h, CrChar*) override {
        std::lock_guard<std::mutex> lock(mu);
        if (!transferring || h != active || n == sdk::CrNotify_ContentsTransfer_Start) return;
        transferDone=true;
        if(n != sdk::CrNotify_ContentsTransfer_Complete) error=n;
        cv.notify_all();
    }
    void OnWarning(CrInt32u w) override {
        if(w==sdk::CrWarning_ContentsTransferMode_Invalid || w==sdk::CrWarning_ContentsTransferMode_DeviceBusy || w==sdk::CrWarning_ContentsTransferMode_StatusError || w==sdk::CrWarning_ContentsTransferMode_CanceledFromCamera) OnError(w);
    }
    ~Camera() { disconnect(); if(enumeration) enumeration->Release(); }
    void disconnect() {
        if(device) {
            sdk::Disconnect(device);
            std::unique_lock<std::mutex> lock(mu);
            bool safe=cv.wait_for(lock, 15s, [&]{return disconnected;});
            lock.unlock();
            // Do not release resources while SDK callbacks could still use them.
            if(!safe) { emit("{\"ok\":false,\"error\":\"Camera did not confirm disconnection; worker stopped. Reconnect camera.\"}"); std::_Exit(3); }
            sdk::ReleaseDevice(device); device=0;
        }
        if(info) { info->Release(); info=nullptr; }
        std::fill(password.begin(),password.end(),'\0'); password.clear();
        std::lock_guard<std::mutex> lock(mu); connected=false; terminal=false; transferring=false; error=0;
    }
    std::string scan() {
        if(device) throw std::runtime_error("Disconnect before scanning again");
        if(enumeration) { enumeration->Release(); enumeration=nullptr; }
        check(sdk::EnumCameraObjects(&enumeration, 3), "Discovery");
        std::ostringstream o; o << "[";
        if(enumeration) for(CrInt32u i=0;i<enumeration->GetCount();++i) {
            const auto* c=enumeration->GetCameraObjectInfo(i);
            if(i) o << ',';
            auto str=[](const char* p){return std::string(p ? p : "");};
            o << "{\"index\":" << i << ",\"model\":" << quote(str(c->GetModel()))
              << ",\"name\":" << quote(str(c->GetName())) << ",\"uid\":" << quote(str(c->GetGuid())+"|"+str(c->GetMACAddressChar()))
              << ",\"connection\":" << quote(str(c->GetConnectionTypeName()))
              << ",\"ip\":" << quote(str(c->GetIPAddressChar())) << ",\"ssh\":" << (c->GetSSHsupport()==sdk::CrSSHsupport_ON?"true":"false") << "}";
        }
        return o.str()+"]";
    }
    void select(unsigned index) {
        if(device) throw std::runtime_error("Already connected");
        if(!enumeration || index>=enumeration->GetCount()) throw std::runtime_error("Scan and choose a camera first");
        if(info) info->Release();
        const auto* c=enumeration->GetCameraObjectInfo(index);
        info=sdk::CreateCameraObjectInfo(c->GetName(),c->GetModel(),c->GetUsbPid(),c->GetIdType(),c->GetIdSize(),c->GetId(),c->GetConnectionTypeName(),c->GetAdaptorName(),c->GetPairingNecessity(),c->GetSSHsupport());
        if(!info) throw std::runtime_error("Could not retain camera information");
    }
    std::string getFingerprint(unsigned index) {
        select(index);
        if(info->GetSSHsupport()!=sdk::CrSSHsupport_ON) return "";
        char buffer[512]={}; CrInt32u length=0;
        check(sdk::GetFingerprint(info,buffer,&length),"Fingerprint retrieval");
        if(length>=sizeof(buffer)) throw std::runtime_error("Unexpected fingerprint length");
        return std::string(buffer,length);
    }
    void connect(unsigned index, const std::string& username, const std::string& secret, const std::string& approved) {
        select(index);
        fingerprint=approved; user=username; password=secret;
        if(info->GetSSHsupport()==sdk::CrSSHsupport_ON && fingerprint.empty()) throw std::runtime_error("Verify the camera fingerprint before connecting");
        { std::lock_guard<std::mutex> lock(mu); error=0; terminal=false; connected=false; disconnected=false; }
        check(sdk::Connect(info,this,&device,sdk::CrSdkControlMode_ContentsTransfer,sdk::CrReconnecting_OFF,
              user.empty()?nullptr:user.c_str(),password.empty()?nullptr:password.c_str(),fingerprint.empty()?nullptr:fingerprint.c_str(),static_cast<CrInt32u>(fingerprint.size())),"Connect");
        std::unique_lock<std::mutex> lock(mu);
        bool done=cv.wait_for(lock,45s,[&]{return connected || terminal;});
        if(!done || !connected || error) {
            auto code=error; lock.unlock(); disconnect();
            if(code) check(static_cast<sdk::CrError>(code),"Connection callback");
            throw std::runtime_error("Camera connection timed out. Confirm pairing on the camera.");
        }
    }
    void requireConnection() { std::lock_guard<std::mutex> lock(mu); if(!connected || terminal) throw std::runtime_error("Camera disconnected. Disconnect, scan, and reconnect."); }
    std::string list() {
        requireConnection();
        sdk::CrMtpFolderInfo* folders=nullptr; CrInt32u count=0;
        check(sdk::GetDateFolderList(device,&folders,&count),"Read date folders");
        std::ostringstream o; o << '['; bool first=true;
        try {
            for(CrInt32u f=0;f<count;++f) {
                sdk::CrContentHandle* handles=nullptr; CrInt32u n=0;
                check(sdk::GetContentsHandleList(device,folders[f].handle,&handles,&n),"Read file handles");
                try {
                    for(CrInt32u i=0;i<n;++i) {
                        sdk::CrMtpContentsInfo c;
                        check(sdk::GetContentsDetailInfo(device,handles[i],&c),"Read file metadata");
                        if(!first) o << ',';
                        first=false;
                        o << "{\"handle\":" << c.handle << ",\"folder\":" << quote(folders[f].folderName?folders[f].folderName:"")
                          << ",\"name\":" << quote(c.fileName?c.fileName:"") << ",\"size\":" << c.contentSize << ",\"captured\":" << quote(std::string(c.dateChar,strnlen(c.dateChar,16))) << "}";
                    }
                } catch(...) { if(handles) sdk::ReleaseContentsHandleList(device,handles); throw; }
                if(handles) sdk::ReleaseContentsHandleList(device,handles);
            }
        } catch(...) { if(folders) sdk::ReleaseDateFolderList(device,folders); throw; }
        if(folders) sdk::ReleaseDateFolderList(device,folders);
        return o.str()+']';
    }
    void pull(sdk::CrContentHandle h, std::string path, std::string name, unsigned timeout) {
        requireConnection();
        if(name.empty() || fs::path(name).filename()!=name || name=="." || name==".." || name.find('\\')!=std::string::npos) throw std::runtime_error("Unsafe destination filename");
        if(!fs::is_directory(path) || fs::exists(fs::path(path)/name)) throw std::runtime_error("Transfer needs an existing, empty staging destination");
        // Per Sony, a fresh detail query is required before PullContentsFile.
        sdk::CrMtpContentsInfo detail; check(sdk::GetContentsDetailInfo(device,h,&detail),"Refresh file metadata");
        { std::lock_guard<std::mutex> lock(mu); active=h; transferring=true; transferDone=false; error=0; }
        auto result=sdk::PullContentsFile(device,h,sdk::CrPropertyStillImageTransSize_Original,path.data(),name.data());
        if(result!=sdk::CrError_None) { std::lock_guard<std::mutex> lock(mu); transferring=false; check(result,"Start file transfer"); }
        auto deadline=std::chrono::steady_clock::now()+std::chrono::seconds(timeout);
        std::unique_lock<std::mutex> lock(mu);
        while(!transferDone && !terminal && std::chrono::steady_clock::now()<deadline) {
            cv.wait_for(lock,250ms);
            lock.unlock();
            std::error_code ec; auto size=fs::file_size(fs::path(path)/name,ec);
            if(!ec) emit("{\"event\":\"progress\",\"bytes\":"+std::to_string(size)+"}");
            lock.lock();
        }
        bool completed=transferDone && !error && !terminal;
        auto code=error;
        if(!transferDone && !terminal) {
            lock.unlock();
            sdk::SendCommand(device,sdk::CrCommandId_CancelContentsTransfer,sdk::CrCommandParam_Down);
            sdk::SendCommand(device,sdk::CrCommandId_CancelContentsTransfer,sdk::CrCommandParam_Up);
            lock.lock(); cv.wait_for(lock,10s,[&]{return transferDone || terminal;});
        }
        bool quiesced=transferDone || terminal;
        transferring=false; lock.unlock();
        if(!completed) {
            disconnect();
            if(!quiesced) { emit("{\"ok\":false,\"error\":\"Transfer timed out; session closed. Reconnect before retrying.\"}"); std::_Exit(4); }
            if(code) check(static_cast<sdk::CrError>(code),"Transfer callback");
            throw std::runtime_error("Transfer interrupted or timed out. Reconnect before retrying.");
        }
    }
};
int main() {
    if(!sdk::Init(0)) { emit("{\"ok\":false,\"error\":\"Sony SDK initialization failed. Check SDK adapter placement.\"}"); return 1; }
    {
        Camera camera; std::string line;
        while(std::getline(std::cin,line)) {
            try {
                std::istringstream in(line); std::string cmd; in >> cmd;
                std::string data="null";
                if(cmd=="scan") data=camera.scan();
                else if(cmd=="fingerprint") { unsigned i; if(!(in>>i)) throw std::runtime_error("Missing camera index"); data=quote(camera.getFingerprint(i)); }
                else if(cmd=="connect") { unsigned i; std::string u,p,f; if(!(in>>i>>u>>p>>f)) throw std::runtime_error("Malformed connect"); camera.connect(i,unhex(u),unhex(p),unhex(f)); std::fill(p.begin(),p.end(),'0'); }
                else if(cmd=="list") data=camera.list();
                else if(cmd=="pull") { unsigned long long h; unsigned t; std::string p,n; if(!(in>>h>>p>>n>>t) || t<5 || t>86400) throw std::runtime_error("Malformed transfer"); camera.pull(static_cast<sdk::CrContentHandle>(h),unhex(p),unhex(n),t); }
                else if(cmd=="disconnect") camera.disconnect();
                else if(cmd=="quit") { camera.disconnect(); emit("{\"ok\":true,\"data\":null}"); break; }
                else throw std::runtime_error("Unknown worker command");
                emit("{\"ok\":true,\"data\":"+data+"}");
            } catch(const std::exception& e) { camera.disconnect(); emit("{\"ok\":false,\"error\":"+quote(e.what())+"}"); }
            std::fill(line.begin(),line.end(),'\0');
        }
    }
    sdk::Release(); return 0;
}
