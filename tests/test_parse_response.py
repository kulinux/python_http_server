from app.model import Response
from app.parse_response import parse_response


def test_parse_ok():
    response = Response.Ok()

    actual = parse_response(response)

    expected = "HTTP/1.1 200 OK\r\n\r\n"
    assert actual == expected


def test_parse_not_found():
    response = Response.NotFound()

    actual = parse_response(response)

    expected = "HTTP/1.1 404 Not Found\r\n\r\n"
    assert actual == expected
