from pathlib import Path

from backupman.config.pkg import Package
pkg_name = Package.Name

class ConfigPaths:
  class System:
    
    Root = Path("/etc").joinpath(f"/{pkg_name}")
    Profile = Root.joinpath("/profiles")

  class User:
    Home = Path.home()
    Local = Home.joinpath(f"/.backupman")
    SmbConfig = Local.joinpath(".smbrc")
    Profiles = Local.joinpath("/profiles")

    def has_home() -> bool:
      home: str = str(ConfigPaths.User.Home)
      home_exists: bool = ConfigPaths.User.Home.exists()

      if home_exists:
        print(f"{home} finns inte/kan inte läsas [av aktuell användare].")
      else:
        print(f"Hittade {home}")

      return home_exists

  def _has_userconfig() -> bool:
    return ConfigPaths.User.has_home()

  def getconfig() -> dict:
    if ConfigPaths._has_userconfig():
      home_dir = ConfigPaths.User.Home
  

