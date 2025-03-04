from app.model import Response


def parse_response(response: Response) -> str:
    if response == Response.Ok():
        return "HTTP/1.1 200 OK\r\n\r\n"
    if response == Response.NotFound():
        return "HTTP/1.1 404 Not Found\r\n\r\n"
    else:
        return "HTTP/1.1 500 Parse Not implemented\r\n\r\n"
