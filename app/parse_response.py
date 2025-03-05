from app.model import Response


EOL = "\r\n"


def parse_response(response: Response) -> str:
    status = f"HTTP/1.1 {response.status} {__message(response.status)}"

    headers = map(
        lambda header: f"{header[0]}: {header[1]}",
        response.headers.items(),
    )

    body = EOL + EOL + response.body if response.body is not None else EOL

    return status + EOL + EOL.join(headers) + body


def __message(status: int) -> str:
    if status == 200:
        return "OK"
    elif status == 404:
        return "Not Found"
    else:
        return "Not implemented"
