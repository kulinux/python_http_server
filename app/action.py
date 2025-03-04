from app.model import Request, Response


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

    else:
        return Response.NotFound()
