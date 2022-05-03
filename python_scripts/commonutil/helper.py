from __future__ import annotations
from pathlib import Path
import json


class File:
    def __init__(self, fl: str):
        self.fl: Path = Path(fl)

    def write(self, txt: str) -> None:
        with open(self.fl, 'w') as f:
            f.write(txt)

    def read(self) -> str:
        with open(self.fl, 'r') as f:
            return f.read()

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
