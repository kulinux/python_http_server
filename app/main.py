import socket
import asyncio

from app.parse_request import parse_request
from app.parse_response import parse_response
from app.action import action


async def __process_con(conn: socket.socket):
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
    print("Starting on port 4221!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        (conn, _) = server_socket.accept()  # wait for client
        asyncio.run(__process_con(conn))


if __name__ == "__main__":
    main()
