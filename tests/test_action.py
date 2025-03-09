from app.action import action
from app.model import Request, Response
from unittest.mock import Mock, patch
from app.files import read_file


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


def test_read_file():
    with patch("app.routes.read_file") as mock:
        request = Request("GET", "/files/foo.txt")

        mock.return_value = "content"

        actual = action(request)

        mock.assert_called_with("www", "foo.txt")

        assert actual == Response.Ok().with_body("content").with_header(
            "Content-Length", "7"
        )


def test_read_file_not_exists():
    with patch("app.routes.read_file") as mock:
        request = Request("GET", "/files/foo.txt")
        mock.return_value = None

        actual = action(request)

        assert actual == Response.NotFound()
