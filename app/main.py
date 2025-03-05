import socket

from app.parse_request import parse_request
from app.parse_response import parse_response
from app.action import action


def __process_con(conn: socket.socket):
    contentAsBytes = conn.recv(10000)

    content = contentAsBytes.decode("utf-8")

    request = parse_request(content)

    if request is None:
        raise Exception("request is None")

    response = action(request)
    content_response = parse_response(response)
    conn.send(content_response.encode("utf-8"))

    conn.close()


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (conn, _) = server_socket.accept()  # wait for client
    __process_con(conn)


if __name__ == "__main__":
    main()
