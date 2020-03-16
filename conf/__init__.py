import sys, os
from configparser import ConfigParser
from pathlib import Path

from conf import configpaths

def read_config() -> SmbConfig:
  smbrc = configpaths.SmbRc

  if not smbrc.exists():
    etc_path = str(configpaths.Etc)
    raise IOError(f".smbrc finns inte i katalogen {etc_path}.")

  confparser = ConfigParser()
  confparser.read(str(smbrc.resolve()))

  local = confparser["Local"]
  Local = {
    "MountPath": local.get("MountPath")
  }

  windows = confparser["Windows"]
  Windows = {
    "Username": windows.get("Username"),
    "Password": windows.get("Password"),
    "Share": windows.get("Share")
  }

  conf = {
    "Local": Local,
    "Windows": Windows
  }

  return conf
