import sys
import os
from configparser import ConfigParser
from pathlib import Path

from backupman.config import smbconfig


def load_smbconfig():
    smb_config = None

    try:
        smb_config = smbconfig.load_config()
    except IOError as e:
        print(f"Kunde inte läsa SMB-konfig: {e}")
    except Exception:
        print("Något gick snett.")

    return smb_config
