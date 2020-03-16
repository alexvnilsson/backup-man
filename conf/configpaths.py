from pathlib import Path

Etc = Path("/etc/backup-man")
SmbRc = Etc.joinpath(".smbrc")
Profiles = Etc.joinpath("profiles")