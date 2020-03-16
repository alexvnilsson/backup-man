from typing import TypedDict

class SmbConfigLocal(TypedDict):
  mount_path: str

class SmbConfigWindows(TypedDict):
  username: str
  password: str
  share: str

class SmbConfig(TypedDict):
  local: SmbConfigLocal
  windows: SmbConfigWindows
