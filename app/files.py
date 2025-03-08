from typing import Optional
from os.path import exists


def read_file(dir: str, filename: str) -> Optional[str]:
    abs_path = dir + "/" + filename
    if not exists(abs_path):
        return None
    with open(abs_path, "r", encoding="utf-8") as file:
        return file.read()
