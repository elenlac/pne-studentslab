import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        message = f"Connection to SERVER at {self.ip}, PORT: {self.port}"
        return message

    def ping(self):
        print("OK!")

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # we create the socket

        s.connect((self.ip, self.port))  # now the connection to the server is established

        s.send(str.encode(msg))  # we send the data (the message)

        response = s.recv(2048).decode("utf-8")  # we receive data (the response)

        s.close()  # finally, we close the socket and return the response received from the server

        return response




