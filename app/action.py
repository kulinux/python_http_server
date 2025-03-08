from app.model import Request, Response
from app.files import read_file


def action(request: Request) -> Response:
    if request.path == "/":
        return Response.Ok()
    elif request.path.startswith("/echo"):
        body = request.path.removeprefix("/echo/")
        return (
            Response.Ok()
            .with_header("Content-Length", str(len(body)))
            .with_header("Content-Type", "text/plain")
            .with_body(body)
        )
    elif request.path.startswith("/files"):
        filename = request.path.removeprefix("/files/")
        content = read_file("www", filename)
        if content is None:
            return Response.NotFound()
        return (
            Response.Ok()
            .with_body(content)
            .with_header("Content-Length", str(len(content)))
        )
    else:
        return Response.NotFound()
