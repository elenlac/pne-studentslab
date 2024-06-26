import socket
import termcolor
from pathlib import Path
import os

IP = "127.0.0.1"
PORT = 8080


def process_client(client_socket):
    try:
        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode()
        lines = request.splitlines()
        request_line = lines[0]
        print("Request line: ", end="")
        termcolor.cprint(request_line, 'green')
        slices = request_line.split(' ')
        method = slices[0]
        resource = slices[1]
        version = slices[2]

        # DEPENDING ON THE RESOURCE, THE SERVER WILL DO THE FOLLOWING: DIFFERENCE IS THAT WE NOW ADD CYTOSINE
        if resource == "/info/A":
            filename = os.path.join("html", "A.html")
            body = Path(filename).read_text()
            status_line = "HTTP/1.1 200 OK\n"
        elif resource == "/info/C":
            filename = os.path.join("html", "C.html")
            body = Path(filename).read_text()
            status_line = "HTTP/1.1 200 OK\n"
        else:
            filename = os.path.join("html", "basic_index.html")
            body = Path(filename).read_text()
            status_line = "HTTP/1.1 404 Not found\n"

        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response = f"{status_line}{header}\n{body}"
        response_bytes = response.encode()
        client_socket.send(response_bytes)
    except IndexError:
        pass


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print("SEQ Server configured!")

try:
    while True:
        print("Waiting for clients...")

        (client_socket, client_address) = server_socket.accept()
        process_client(client_socket)
        client_socket.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()
