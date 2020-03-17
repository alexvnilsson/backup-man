from pathlib import Path
from backupman.config.pkg import Package

# Variabler
pkg_name = Package.Name
rules_ext = Package.RulesExt

class ConfigPaths:
    class System:
        Root = Path("/etc").joinpath(f"{pkg_name}")
        SmbConfig = Root.joinpath(rules_ext)
        Rules = Root.joinpath("rules")

    class User:
        Home = Path.home()
        Local = Home.joinpath(f".backupman")
        SmbConfig = Local.joinpath(rules_ext)
        Rules = Local.joinpath("rules")
