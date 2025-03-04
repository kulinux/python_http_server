from dataclasses import dataclass, field
import dataclasses
from typing import Dict, Optional


@dataclass
class Request:
    method: str
    path: str


@dataclass
class Response:
    status: int
    body: Optional[str] = None
    headers: Dict[str, str] = field(default_factory=dict)

    @staticmethod
    def Ok() -> "Response":
        return Response(200)

    @staticmethod
    def NotFound() -> "Response":
        return Response(404)

    def with_body(self, body: str) -> "Response":
        return dataclasses.replace(self, body=body)

    def with_header(self, header: str, value: str) -> "Response":
        new_headers = self.headers.copy()
        new_headers[header] = value
        return dataclasses.replace(self, headers=new_headers)
