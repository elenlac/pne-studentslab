"""This file is our module, that will be imported in all the exercises"""


class Client:  # represents a client(sends messages to the server) in a server-client model
    def __init__(self, server_ip: str, server_port: int):  # IP as a string and PORT as an integer
        # the constructor stores the address to which the client connects:
        self.server_ip = server_ip
        self.server_port = server_port

    def __str__(self):
        return f"Connection to SERVER at {self.server_ip}, PORT: {self.server_port}"

    # NOT PREDEFINED METHODS:
    def ping(self):  # it appears in yellow since it is a static method as you don't use self
        print("OK!")

    """   
    @staticmethod  # a method that belongs to a class, not its instances.
    def ping():  
        print("OK!")
        
    # at the time of calling it you could either:
        c.ping()
        Client.ping()
    """

    def talk(self, msg):  # for each talk a new socket will be created and so a new port will be assigned
        import socket

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # we create the socket of the client

        client_socket.connect((self.server_ip, self.server_port))  # now the connection to the server is established

        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)  # we turn it into bytes with str.encode, then we send the data in bytes to server

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")  # we receive data from the server and then turn it into a str

        client_socket.close()  # we close the socket (finish communication) and return the response of the server

        return response
