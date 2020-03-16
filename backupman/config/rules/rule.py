from typing import TypedDict, List

class Rule(TypedDict):
  name: str
  include: List[str]