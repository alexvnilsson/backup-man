import sys
import os
from configparser import ConfigParser
from pathlib import Path

from backupman.config import paths
from backupman.config.paths import ConfigPaths
from backupman.config.smbconfig.smbrc import SmbConfig, SmbConfigLocal, SmbConfigWindows


def load_config() -> SmbConfig:
    try:
        configpath = paths.get_configpath()
    except IOError as e:
        print(f"Kunde inte ladda SMB-konfig.: {e}")

    confparser = ConfigParser()
    confparser.read(configpath)

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

    smbconfig: SmbConfig = {
        "Local": Local,
        "Windows": Windows
    }

    return smbconfig
