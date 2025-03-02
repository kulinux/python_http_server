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
