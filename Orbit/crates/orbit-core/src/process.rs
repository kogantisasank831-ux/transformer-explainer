use crate::{Cancellation, Error};
use std::{
    fs::File,
    process::{Command, Stdio},
    time::{Duration, Instant},
};

/// No shell interpolation. Separate logs avoid pipe deadlocks on large output.
pub fn run(command: &mut Command, cancel: &Cancellation) -> Result<(), Error> {
    cancel.check()?;
    #[cfg(unix)]
    {
        use std::os::unix::process::CommandExt;
        command.process_group(0);
    }
    #[cfg(windows)]
    {
        use std::os::windows::process::CommandExt;
        command.creation_flags(0x08000000); // CREATE_NO_WINDOW
    }
    let log = tempfile::NamedTempFile::new()?;
    let output = log.reopen()?;
    command
        .stdin(Stdio::null())
        .stdout(Stdio::from(output.try_clone()?))
        .stderr(Stdio::from(output));
    let mut child = command.spawn()?;
    let started = Instant::now();
    loop {
        let interrupted = cancel
            .check()
            .err()
            .or_else(|| (started.elapsed() > Duration::from_secs(600)).then_some(Error::Timeout));
        if let Some(error) = interrupted {
            #[cfg(unix)]
            unsafe {
                libc::kill(-(child.id() as i32), libc::SIGKILL);
            }
            #[cfg(windows)]
            {
                let _ = Command::new("taskkill")
                    .args(["/PID", &child.id().to_string(), "/T", "/F"])
                    .stdout(Stdio::null())
                    .stderr(Stdio::null())
                    .status();
            }
            let _ = child.kill();
            let _ = child.wait();
            return Err(error);
        }
        if let Some(status) = child.try_wait()? {
            if status.success() {
                return Ok(());
            }
            use std::io::Read;
            let mut message = String::new();
            File::open(log.path())?
                .take(12_000)
                .read_to_string(&mut message)?;
            return Err(Error::Engine(if message.trim().is_empty() {
                format!("Conversion engine exited with {status}")
            } else {
                message.trim().into()
            }));
        }
        std::thread::sleep(Duration::from_millis(80));
    }
}

#[cfg(all(test, unix))]
mod tests {
    use super::*;
    #[test]
    fn running_process_can_be_cancelled() {
        let token = Cancellation::default();
        let other = token.clone();
        let signal = std::thread::spawn(move || {
            std::thread::sleep(Duration::from_millis(120));
            other.cancel();
        });
        let start = Instant::now();
        let result = run(Command::new("/bin/sh").args(["-c", "sleep 30"]), &token);
        signal.join().unwrap();
        assert!(matches!(result, Err(Error::Cancelled)));
        assert!(start.elapsed() < Duration::from_secs(3));
    }
}
