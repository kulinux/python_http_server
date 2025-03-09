from abc import ABC, abstractmethod
from typing import List
from app.model import Request, Response
from app.files import read_file


class Action(ABC):
    @abstractmethod
    def match(self, request: Request) -> bool:
        pass

    @abstractmethod
    def action(self, request: Request) -> Response:
        pass


class RootPath(Action):
    def match(self, request: Request) -> bool:
        return request.path == "/"

    def action(self, request: Request) -> Response:
        return Response.Ok()


class Echo(Action):
    def match(self, request: Request) -> bool:
        return request.path.startswith("/echo")

    def action(self, request: Request) -> Response:
        body = request.path.removeprefix("/echo/")
        return (
            Response.Ok()
            .with_header("Content-Length", str(len(body)))
            .with_header("Content-Type", "text/plain")
            .with_body(body)
        )


class Files(Action):
    def match(self, request: Request) -> bool:
        return request.path.startswith("/files")

    def action(self, request: Request) -> Response:
        filename = request.path.removeprefix("/files/")
        content = read_file("www", filename)
        if content is None:
            return Response.NotFound()
        return (
            Response.Ok()
            .with_body(content)
            .with_header("Content-Length", str(len(content)))
        )


installed_routes: List[Action] = [RootPath(), Echo(), Files()]
