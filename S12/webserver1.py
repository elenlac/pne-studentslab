import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(client_socket):
    # HERE WE PARSE THE CLIENT'S REQUEST
    request_bytes = client_socket.recv(2048)  # we store the bytes of the request made by the client (max 2048)
    request = request_bytes.decode()  # "Get / HTTP/1.1...."
    print("Message FROM CLIENT: ")
    lines = request.splitlines()  # ["Get / HTTP/1.1....", "Host", ...]
    request_line = lines[0]  # takes from the list of lines the first lines, storing it in a variable
    print("Request line: ", end="")  # deletes the default \n of the end
    termcolor.cprint(request_line, 'green')

    # SERVER BUILDS A RESPONSE MESSAGE, NOW IT KNOWS HOW TO TREAT THE HTTP PROTOCOL
    body = "Hello from my first web server!\n"  # plain text, not html, this property is determined in the first field
    status_line = "HTTP/1.1 200 OK\n"  # contains
    header = "Content-Type: text/plain\n"  # we are putting two fields
    header += f"Content-Length: {len(body)}\n"  # one character occupies one byte, specifies how much space it takes
    response = f"{status_line}{header}\n{body}"  # we put the mandatory blank line
    response_bytes = response.encode()
    client_socket.send(response_bytes)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print("ECHO Server configured!")

try:
    while True:
        print("Waiting for clients....")

        (client_socket, client_address) = server_socket.accept()
        process_client(client_socket)
        client_socket.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()
