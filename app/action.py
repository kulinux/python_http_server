from app.model import Request, Response


def action(request: Request) -> Response:
    if request.path == "/":
        return Response.Ok()
    else:
        return Response.NotFound()
