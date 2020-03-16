from typing import List, Any
import glob
import json
from pathlib import Path
import os.path
from conf import configpaths

CONF_FIELDS = [
  'name',
  'include'
]

CONF_FIELDS_INPUT_PROMPT = [
  'include'
]

def __get_path(profile_name: str) -> str:
  return str(configpaths.Profiles.joinpath(Path(profile_name).with_suffix(".prof")))

def list_profiles() -> List[str]:
  profiles: List[str] = []
  profiles_path = configpaths.Profiles

  profs = glob.glob(str(profiles_path.joinpath("*.prof")))

  for p in profs:
    pp = Path(p)
    profiles.append(pp.stem)

  return profiles

def is_created(profile_name: str) -> bool:
  profile_path = __get_path(profile_name)

  return os.path.exists(str(profile_path))

def read_profile(profile_name: str):
  profile_path = __get_path(profile_name)
  profile_data = None
  
  with open(profile_path, 'r') as pf:
    profile_data = json.load(pf)

  if profile_data is None:
    return None

  return profile_data

def write_profile(profile_name: str, profile_include: List[str]):
  profile_path = __get_path(profile_name)

  profile_data = {
    'name': profile_name,
    'include': profile_include
  }

  with open (profile_path, 'w') as pf:
    json.dump(profile_data, pf)
    pf.close()

def update_profile(profile_name: str, field: str, value: Any):
  profile_path = __get_path(profile_name)

  with open(profile_path, 'r+') as pf:
    profile_data = json.load(pf)

    if profile_data is None:
      raise Exception(f"Kunde inte läsa innehållet av profilen '{profile_name}'!'")

    tmp = profile_data[field]
    profile_data[field] = value

    pf.seek(0)
    json.dump(profile_data, pf)
    pf.truncate()

def get_files(profile: dict):
  print(profile['include'])