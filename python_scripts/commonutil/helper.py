from __future__ import annotations
from pathlib import Path
import json
from typing import List

class File:
    def __init__(self, fl: str):
        self.fl: Path = Path(fl)

    def write(self, txt: str) -> None:
        with open(self.fl, 'w') as f:
            f.write(txt)

    def read(self) -> str:
        with open(self.fl, 'r') as f:
            return f.read()

    def readlines(self) -> List[str]:
        return self.read().splitlines()

    def append(self, txt: str) -> None:
        with open(self.fl, 'a') as f:
            f.write(txt)

    def load_json(self) -> dict:
        with open(self.fl, 'r') as f:
            return json.load(f)


class Folder:
    def __init__(self, fldr):
        self.fldr: Path = Path(fldr)

    def get_dirs(self) -> list[Folder]:
        return [Folder(x) for x in self.fldr.iterdir() if x.is_dir()]


def dummy(*args, **kwargs):
    pass


def get_choice_from_user(title:str, options: List[str]) -> str:
    print( f'{"="*5} {title} {"="*5}' )
    for i,v in enumerate(options,1):
        print( f'{i} {v}')
    ch = input('Enter choice : ')
    return options[int(ch)-1]
