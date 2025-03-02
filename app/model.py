from dataclasses import dataclass


@dataclass
class Request:
    method: str
    path: str


@dataclass
class Response:
    status: int

    @staticmethod
    def Ok():
        return Response(200)

    @staticmethod
    def NotFound():
        return Response(404)
