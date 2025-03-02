import socket
from app.parse import parse_request  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (conn, _) = server_socket.accept()  # wait for client

    contentAsBytes = conn.recv(10000)

    content = contentAsBytes.decode("utf-8")

    request = parse_request(content)

    ok = "HTTP/1.1 200 OK\r\n\r\n"
    not_found = "HTTP/1.1 404 Not Found\r\n\r\n"

    if request is None:
        raise Exception("request is None")
    elif request.path == "/":
        response = ok
    else:
        response = not_found

    conn.send(response.encode("utf-8"))

    conn.close()


if __name__ == "__main__":
    main()
