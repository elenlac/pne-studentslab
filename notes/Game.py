import socket
import random

"""HERE WE HAVE THE CLASS NUMBERGUESSER, OUR GAME:"""
class NumberGuesser:
    MIN = 1
    MAX = 100

    def __init__(self):
        self.secret_number = random.randint(NumberGuesser.MIN, NumberGuesser.MAX)  # generates a random number
        self.attempts = []  # here the number of attempts made by the client will be stored
        self.guessed = False  # the initial value of attribute guessed will be false until it is actually guessed(=True)

    def __str__(self):
        return f"Secret number: {self.secret_number} - Attempts: {self.attempts}"

    def guess(self, number):  # receives the number of the client, adds it to attempts list, and responds
        self.attempts.append(number)
        if number < self.secret_number:
            string = "Higher"
        elif number > self.secret_number:
            string = "Lower"
        else:
            self.guessed = True
            x = len(self.attempts)
            string = f"You won after {x} attempts"
        return string

    def is_guessed(self):
        return self.guessed


"""HERE WE HAVE THE SERVER CODE:"""

IP = "127.0.0.1"
PORT = 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen()
    print("'Guess the number' server configured!")

    while True:
        print(f"Waiting for connections at {IP}, {PORT}")
        (clientsocket, address) = serversocket.accept()

        number = NumberGuesser()  # server creates a new object of this class everytime a client connects

        guessed = False  # establishes guessed as false
        while not guessed:  # enters the loop

            # Receive the message from client
            request_bytes = clientsocket.recv(2048)
            request = request_bytes.decode("utf-8")
            int_request = int(request)
            print(f"Guess from client: {int_request}")

            # Send the response to the client
            response = number.guess(int_request)  # response is the string returned by the guess method
            response_bytes = clientsocket.send(response.encode())

            print(number)  # the object is printed

            if number.is_guessed():  # if it has been guessed, then the boolean turns True to exit the loop
                guessed = True
        clientsocket.close()

except socket.error:
    print(f"Problems using ip {IP} port {PORT}. Is the IP correct? Do you have port permission?")
except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

