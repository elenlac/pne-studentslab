import socket
import random

PORT = 8081
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5
number_con = 0


class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def __str__(self):
        pass

    def guess(self, number):
        if number < self.secret_number:
            self.attempts.append(number)
            string = "Higher"
        elif number > self.secret_number:
            self.attempts.append(number)
            string = "Lower"
        else:
            x = len(self.attempts)
            string = f"You won after {x} attempts"

        return string


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print(f"Waiting for connections at {IP}, {PORT}")
        (clientsocket, address) = serversocket.accept()

        number_con += 1
        print(f"CONNECTION: {number_con}. From the address: {address}")  # address= ip_client + port_client
        game = NumberGuesser()

        flag = True
        while flag:
            # Receive the message
            msg = clientsocket.recv(2048).decode("utf-8")
            print(f"Message from client: {msg}")

            # Send the message
            msg = int(msg)
            guess = game.guess(msg)
            clientsocket.send(str.encode(guess))
            flag = False

        clientsocket.close()

except socket.error:
    print(f"Problems using ip {IP} port {PORT}. Is the IP correct? Do you have port permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

