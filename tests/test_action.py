from app.action import action
from app.model import Request, Response


def test_ok_when_root_path():
    request = Request("GET", "/")

    actual = action(request)

    assert actual == Response.Ok()


def test_nok_when_no_root_path():
    request = Request("GET", "/asdf")

    actual = action(request)

    assert actual == Response.NotFound()


def test_echo():
    request = Request("GET", "/echo/abcd")

    actual = action(request)

    assert actual == Response.Ok().with_body("abcd").with_header(
        "Content-Length", "4"
    ).with_header("Content-Type", "text/plain")
