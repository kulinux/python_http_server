from dataclasses import dataclass
from typing import Optional


@dataclass
class Request:
    method: str
    path: str


def parse_request(content: str) -> Optional[Request]:
    (head, *_) = content.split("\n")

    first_line = head.split()
    if len(first_line) != 3:
        return None

    (method, path, *_) = head.split()
    return Request(method, path)
