from app.parse import Request, parse_request


def test_parse_get_request():
    content = "GET /index.html HTTP/1.1\r\n\r\n"

    expected = Request("GET", "/index.html")

    actual = parse_request(content)

    assert actual == expected


def test_parse_post_request():
    content = "POST /index.html HTTP/1.1\r\n\r\n"

    expected = Request("POST", "/index.html")

    actual = parse_request(content)

    assert actual == expected


def test_parse_path():
    content = "GET /foo.html HTTP/1.1\r\n\r\n"

    expected = Request("GET", "/foo.html")

    actual = parse_request(content)

    assert actual == expected


def test_wrong_first_line_format():
    content = "GET/foo.html HTTP/1.1\r\n\r\n"

    expected = None

    actual = parse_request(content)

    assert actual == expected
