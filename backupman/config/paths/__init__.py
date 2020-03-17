# pylint: skip-no-method-argument

import os
from pathlib import Path
from backupman.config.paths.configpaths import ConfigPaths


def resolve(p: Path = None):
    if p is None:
        raise TypeError("Förväntade mig en Path, fick ingenting.")

    if isinstance(p, Path):
        return str(p.resolve())


class System:
    @staticmethod
    def hasroot() -> bool:
        return ConfigPaths.System.Root.exists()

    @staticmethod
    def hasrules() -> bool:
        if System.hasroot():
            return ConfigPaths.System.Rules.exists()

        return False

    @staticmethod
    def hasconfig() -> bool:
        return ConfigPaths.User.SmbConfig.exists()


class User:
    @staticmethod
    def hashome() -> bool:
        home: str = str(ConfigPaths.User.Home)
        home_exists: bool = ConfigPaths.User.Home.exists()

        return home_exists

    @staticmethod
    def haslocal() -> bool:
        if User.hashome():
            return ConfigPaths.User.Local.exists()

        return False

    @staticmethod
    def hasrules() -> bool:
        if User.haslocal():
            return ConfigPaths.User.Rules.exists()

        return False

    @staticmethod
    def hasconfig() -> bool:
        if User.hashome():
            return ConfigPaths.User.SmbConfig.exists()
        else:
            return False


def make_userconfig():
    home_dir = ConfigPaths.User.Home
    local_dir = ConfigPaths.User.Local
    rules_dir = ConfigPaths.User.Rules

    if home_dir.exists():
        if not local_dir.exists():
            os.mkdir(str(local_dir))

        if not rules_dir.exists():
            os.mkdir(str(rules_dir))


def get_root() -> Path:
    if User.haslocal():
        return ConfigPaths.User.Local
    elif System.hasroot():
        return ConfigPaths.System.Root

def get_rulespath() -> Path:
    if User.hasrules():
        return ConfigPaths.User.Rules
    elif System.hasrules():
        return ConfigPaths.System.Rules
    else:
        raise IOError("Finns varken system- eller användar-regler.")


def get_configpath() -> Path:
    configpath_path = None

    if User.haslocal():
        home_dir = ConfigPaths.User.Home
        smbconfig_file = ConfigPaths.User.SmbConfig

        home_stem = home_dir.stem
        smbconfig_stem = smbconfig_file.stem

        if smbconfig_file.exists():
            configpath_path = resolve(smbconfig_file)
        else:
            raise IOError(
                f"{home_stem} finns inte, antaligen inte {smbconfig_stem} heller.")
    else:
        root_dir = ConfigPaths.System.Root
        smbconfig_file = ConfigPaths.System.SmbConfig

        root_stem = root_dir.stem
        smbconfig_stem = smbconfig_file.stem

        if smbconfig_file.exists():
            configpath_path = resolve(smbconfig_file)
        else:
            raise IOError(
                f"{root_stem} finns inte, antaligen inte {smbconfig_stem} heller.")

    return configpath_path
