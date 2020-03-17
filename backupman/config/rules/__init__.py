from typing import List, Any
import glob
import json
from pathlib import Path
import os.path

from backupman.config.pkg import Package
from backupman.config import paths
from backupman.config.paths import ConfigPaths
from backupman.config.rules.rule import Rule

CONF_FIELDS = [
    'name',
    'include'
]

CONF_FIELDS_INPUT_PROMPT = [
    'include'
]


def __get_path(rule_name: str = None) -> Path:
    rules_dir = paths.get_rulespath()
    rules_ext = Package.RulesExt

    if rule_name is not None:
        rules_path = rules_dir.joinpath(Path(rule_name).with_suffix(f".{rules_ext}"))
        return rules_path
    else:
        return rules_dir


def list() -> List[str]:
    r: List[str] = []

    profs = glob.glob(str(__get_path().joinpath("*.prof")))

    for p in profs:
        pp = Path(p)
        r.append(pp.stem)

    return r


def is_created(rule_name: str) -> bool:
    rules_path = __get_path(rule_name)

    return os.path.exists(str(rules_path))


def read(rule_name: str):
    rules_path = __get_path(rule_name)

    with open(rules_path, 'r') as pf:
        rule_data = json.load(pf)

    return rule_data


def remove(rule_name: str):
    if not is_created(rule_name):
        print(f"Kunde inte ta bort regeln {rule_name}: regeln finns inte")
        exit(1)

    try:
        os.remove(__get_path(rule_name))
    except Exception as e:
        print(f"Kunde inte ta bort regeln {rule_name}: {e}")
        exit(1)

def write(rule_name: str, rule_include: List[str]):
    rules_path = __get_path(rule_name)

    rule_data = {
        'name': rule_name,
        'include': rule_include
    }

    with open(rules_path, 'w') as pf:
        json.dump(rule_data, pf)
        pf.close()


def update(rule_name: str, field: str, value: Any):
    rules_path = __get_path(rule_name)

    with open(rules_path, 'r+') as pf:
        rule_data = json.load(pf)

        if rule_data is None:
            raise Exception(
                f"Kunde inte läsa innehållet av regeln '{rule_name}'!'")

        tmp = rule_data[field]
        rule_data[field] = value

        pf.seek(0)
        json.dump(rule_data, pf)
        pf.truncate()


def get_files(r: dict):
    print(r['include'])
