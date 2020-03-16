import sys, os
from configparser import ConfigParser
from pathlib import Path

from backupman.config.paths import ConfigPaths
from backupman.config.smbconfig import SmbConfig, SmbConfigLocal, SmbConfigWindows

def read_config() -> dict:
  if ConfigPaths.has_userconfig():
    print("Has home")
  smbrc = configpaths.SmbRc

  if not smbrc.exists():
    etc_path = str(configpaths.Etc)
    raise IOError(f".smbrc finns inte i katalogen {etc_path}.")

  confparser = ConfigParser()
  confparser.read(str(smbrc.resolve()))

  local = confparser["Local"]
  Local: SmbConfigLocal = {
    "MountPath": local.get("MountPath")
  }

  windows = confparser["Windows"]
  Windows: SmbConfigWindows = {
    "Username": windows.get("Username"),
    "Password": windows.get("Password"),
    "Share": windows.get("Share")
  }

  Config: SmbConfig = {
    "Local": Local,
    "Windows": Windows
  }

  return Config
