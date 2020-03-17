#from config.smbconfig import SmbConfig, SmbConfigLocal, SmbConfigWindows
from backupman.config import SmbConfig

def print_keys():
  print(vars(SmbConfig).keys())