import socket
import termcolor
from pathlib import Path
import os

IP = "127.0.0.1"
PORT = 8080


def process_client(client_socket):  # we put the client socket since it is the communication channel
    try:
        request_bytes = client_socket.recv(2048)  # receive bytes from client through its socket
        request = request_bytes.decode()  # this is a str
        lines = request.splitlines()  # take lines received, eliminate \n and create a list of str: ["GET" / HTTP/1.1, ]
        request_line = lines[0]  # we only store the first element from the list, the http request from the client: str
        print("Request line: ", end="")
        termcolor.cprint(request_line, 'green')
        slices = request_line.split(' ')  # divides the og str in several str using as the separator a blank space: list
        method = slices[0]
        resource = slices[1]  # same as path
        version = slices[2]

        # DEPENDING ON THE RESOURCE, THE SERVER WILL DO THE FOLLOWING:
        if resource == "/info/A":  # resource is the path, in this case it is not a single "/" but "/info/A"
            filename = os.path.join("html", "A.html")  # regardless of the os, join generates a path to the file I want
            body = Path(filename).read_text()  # remember Path is a class from pathlib module, used to work with paths
            # here we are creating an object of the Path class, we are calling the init,
            # and we call the method "read_text()" that reads it and gives back the content in a single str
            status_line = "HTTP/1.1 200 OK\n"  # Version: HTTP/1.1 , Status Code: 200 , Status: OK
        else:  # the server doesn't have the resource
            filename = os.path.join("html", "basic_index.html")
            body = Path(filename).read_text()
            status_line = "HTTP/1.1 404 Not found\n"

        # THESE ARE ALWAYS EXECUTED
        # headers: field strings and their value, these gives client info about the type of content how much it occupies
        header = "Content-Type: text/html\n"  # store a str that contains a field and a value
        # indicates that the server will send the client as content text type in html format, responds with web page
        header += f"Content-Length: {len(body)}\n"  # calculates all the bytes occupied by the body sent by the server
        response = f"{status_line}{header}\n{body}"  # we respond the client
        response_bytes = response.encode()
        client_socket.send(response_bytes)
    except IndexError:
        pass


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create the server socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # to reuse the PORT and not receive an error

server_socket.bind((IP, PORT))
server_socket.listen()

print("DNA Bases Server configured!")

try:
    while True:
        print("Waiting for clients...")

        (client_socket, client_address) = server_socket.accept()
        process_client(client_socket)  # this function performs the dialogue with the client
        client_socket.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()
