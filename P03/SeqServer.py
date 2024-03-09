import socket
from termcolor import *
from Seq3 import Seq
import os

IP = "127.0.0.1"
PORT = 8080
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
BASES = ["A", "C", "T", "G"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("SEQ Server configured")
    while True:
        print(f"Waiting for clients...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request_from_client = request_bytes.decode("utf-8")

        lines = request_from_client.splitlines()  # to remove the \n that may appear and obtain a list with one element

        slices = lines[0].split(" ")  # our sep is a blank space and slices will also be a list with up to 2 elements
        command = slices[0]  # since slices will be a list, the first item will be the command
        print(colored(command, "green"))

        response = None  # in the first place, response is none, but when we get into "if" it gets a value
        if command == "PING":
            response = "OK!\n"

        elif command == "GET":
            n = int(slices[1])  # we get the position of the second element given by the client: THE NUMBER OF THE GENE
            gene = GENES[n]  # according to the number given, we locate the gene of the GENE list

            s = Seq()
            filename = os.path.join("..", "sequences", gene + ".txt.fa")  # build the name of the file
            s.read_fasta(filename)
            response = str(s)  # return our object as a string

        elif command == "INFO":
            seq = str(slices[1])
            s = Seq(seq)
            response = f"Sequence: {s}\nTotal length: {s.len()}"
            for b in BASES:
                percentage = ((s.count_base(b) / s.len()) * 100)
                percentage_rounded = round(percentage, 1)
                response += f"\n {b}: {s.count_base(b)} ({percentage_rounded}%)"

        elif command == "COMP":
            seq = str(slices[1])
            s = Seq(seq)
            response = str(s.complement())

        elif command == "REV":
            seq = str(slices[1])
            s = Seq(seq)
            response = str(s.reverse())

        elif command == "GENE":
            name = str(slices[1])

            if name in GENES:
                s = Seq()
                filename = os.path.join("..", "sequences", name + ".txt.fa")  # build the name of the file
                s.read_fasta(filename)
                response = str(s)

        print(response)
        response_bytes = response.encode()
        client_socket.send(response_bytes)  # the response must be sent to the client_socket
        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()
