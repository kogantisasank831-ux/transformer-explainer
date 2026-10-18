// Test-only SDK simulator. Uses headers from an independently downloaded Sony SDK.
// This file is original test code; no Sony SDK headers/libraries are redistributed.
#include "CameraRemote_SDK.h"
#include "IDeviceCallback.h"
#include <atomic>
#include <chrono>
#include <cstring>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <string>
#include <thread>
namespace s = SCRSDK;
using namespace std::chrono_literals;
namespace {
s::IDeviceCallback* callback=nullptr;
std::thread transfer;
std::atomic<bool> cancel{false};
std::string scenario() { const char* p=std::getenv("ALPHALINK_SIM_SCENARIO"); return p?p:"success"; }
class Info final : public s::ICrCameraObjectInfo {
public:
 void Release() override { delete this; }
 CrChar* GetName() const override { return const_cast<char*>("Camera \"test\""); }
 CrInt32u GetNameSize() const override { return 13; }
 CrChar* GetModel() const override { return const_cast<char*>("ILCE-6700"); }
 CrInt32u GetModelSize() const override { return 10; }
 CrInt16 GetUsbPid() const override { return 1; }
 CrInt8u* GetId() const override { return reinterpret_cast<CrInt8u*>(const_cast<char*>("test-id")); }
 CrInt32u GetIdSize() const override { return 8; }
 CrInt32u GetIdType() const override { return 1; }
 CrInt32u GetConnectionStatus() const override { return 0; }
 CrChar* GetConnectionTypeName() const override { return const_cast<char*>("IP"); }
 CrChar* GetAdaptorName() const override { return const_cast<char*>("Cr_PTP_IP"); }
 CrChar* GetGuid() const override { return const_cast<char*>("test-guid"); }
 CrChar* GetPairingNecessity() const override { return const_cast<char*>("no"); }
 CrInt16u GetAuthenticationState() const override { return 0; }
 CrInt32u GetSSHsupport() const override { return s::CrSSHsupport_ON; }
 CrInt32u GetIPAddress() const override { return 0; }
 CrChar* GetIPAddressChar() const override { return const_cast<char*>("192.0.2.1"); }
 CrInt32u GetIPAddressCharSize() const override { return 10; }
 CrInt8u* GetMACAddress() const override { static CrInt8u b[6]={}; return b; }
 CrInt32u GetMACAddressSize() const override { return 6; }
 CrChar* GetMACAddressChar() const override { return const_cast<char*>("00:11:22:33:44:55"); }
 CrInt32u GetMACAddressCharSize() const override { return 18; }
};
class Enumeration final : public s::ICrEnumCameraObjectInfo {
 Info info;
public:
 CrInt32u GetCount() const override {return 1;}
 const s::ICrCameraObjectInfo* GetCameraObjectInfo(CrInt32u) const override {return &info;}
 void Release() override {delete this;}
};
}
namespace SCRSDK {
bool Init(CrInt32u) {return true;}
bool Release() {return true;}
CrError EnumCameraObjects(ICrEnumCameraObjectInfo** p, CrInt8u) {*p=new Enumeration;return CrError_None;}
ICrCameraObjectInfo* CreateCameraObjectInfo(CrChar*,CrChar*,CrInt16,CrInt32u,CrInt32u,CrInt8u*,CrChar*,CrChar*,CrChar*,CrInt32u) {return new Info;}
CrError GetFingerprint(ICrCameraObjectInfo*,char* b,CrInt32u* n) {std::string f="SHA256:SIMULATED";std::memcpy(b,f.data(),f.size());*n=f.size();return CrError_None;}
CrError Connect(ICrCameraObjectInfo*,IDeviceCallback* cb,CrDeviceHandle* h,CrSdkControlMode mode,CrReconnectingSet,const char*,const char*,const char*,CrInt32u,const CrInt16u*) {
 if(mode!=CrSdkControlMode_ContentsTransfer)return CrError_Generic_NotSupported;
 callback=cb;*h=1;
 std::thread([] {std::this_thread::sleep_for(20ms);if(scenario()=="connect-error") callback->OnError(CrError_Generic_NotSupported);else callback->OnConnected(static_cast<DeviceConnectionVersioin>(0));}).detach();
 return CrError_None;
}
CrError Disconnect(CrDeviceHandle) {
 cancel=true;
 if(transfer.joinable()) transfer.join();
 callback->OnDisconnected(0);return CrError_None;
}
CrError ReleaseDevice(CrDeviceHandle) {return CrError_None;}
CrMtpFolderInfo::CrMtpFolderInfo():handle(1),folderNameSize(11),folderName(nullptr) {}
CrMtpFolderInfo::~CrMtpFolderInfo() {delete[] folderName;}
CrMtpContentsInfo::CrMtpContentsInfo():handle(7),parentFolderHandle(1),contentSize(8),dateChar{},width(0),height(0),fileNameSize(0),fileName(nullptr) {}
CrMtpContentsInfo::~CrMtpContentsInfo() {delete[] fileName;}
CrError GetDateFolderList(CrDeviceHandle,CrMtpFolderInfo** p,CrInt32u* n) {*p=new CrMtpFolderInfo[1];(*p)[0].folderName=new char[11];std::strcpy((*p)[0].folderName,"2026-10-18");*n=1;return CrError_None;}
CrError ReleaseDateFolderList(CrDeviceHandle,CrMtpFolderInfo* p) {delete[] p;return CrError_None;}
CrError GetContentsHandleList(CrDeviceHandle,CrFolderHandle,CrContentHandle** p,CrInt32u* n) {*p=new CrContentHandle[1]{7};*n=1;return CrError_None;}
CrError ReleaseContentsHandleList(CrDeviceHandle,CrContentHandle* p) {delete[] p;return CrError_None;}
CrError GetContentsDetailInfo(CrDeviceHandle,CrContentHandle h,CrMtpContentsInfo* p) {p->handle=h;p->fileName=new char[13];std::strcpy(p->fileName,"DSC00001.JPG");std::strcpy(p->dateChar,"20261018T153000");return CrError_None;}
CrError PullContentsFile(CrDeviceHandle,CrContentHandle h,CrPropertyStillImageTransSize size,CrChar* dir,CrChar* name) {
 if(size!=CrPropertyStillImageTransSize_Original)return CrError_Generic_NotSupported;
 if(transfer.joinable())transfer.join();cancel=false;
 auto target=std::filesystem::path(dir)/name;
 transfer=std::thread([h,target] {
   callback->OnNotifyContentsTransfer(CrNotify_ContentsTransfer_Start,h,nullptr);
   std::ofstream stream(target,std::ios::binary);stream<<"DATA";stream.flush();
   auto loops=scenario()=="timeout"?100:3;
   for(int i=0;i<loops && !cancel;i++)std::this_thread::sleep_for(100ms);
   if(scenario()=="transfer-error" || cancel) {stream.close(); callback->OnNotifyContentsTransfer(CrWarning_ContentsTransferMode_CanceledFromCamera,h,nullptr);return;}
   stream<<"END!";stream.close();auto name=target.string(); callback->OnNotifyContentsTransfer(CrNotify_ContentsTransfer_Complete,h,name.data());
 });return CrError_None;
}
CrError SendCommand(CrDeviceHandle,CrInt32u command,CrCommandParam param) {if(command==CrCommandId_CancelContentsTransfer && param==CrCommandParam_Up)cancel=true;return CrError_None;}
}
