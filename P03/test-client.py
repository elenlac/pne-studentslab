from Client3 import Client

practice = 3
exercise = 7

print(f"-----| Practice {practice}, Exercise {exercise} |------")

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8081

N = 5
seq = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

c = Client(SERVER_IP, SERVER_PORT)
print(c)

print(f"* Testing PING...")
response = c.talk("PING")
print(f"{response}\n")

print(f"* Testing GET...")
for n in range(N):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response}")
print(f"\n")

print(f"* Testing INFO...")
response = c.talk(f"INFO {seq}")
print(f"{response}\n")

print(f"* Testing COMP...")
print(f"COMP {seq}")
response = c.talk(f"COMP {seq}")
print(f"{response}\n")

print(f"* Testing REV...")
print(f"REV {seq}")
response = c.talk(f"REV {seq}")
print(f"{response}\n")

print(f"* Testing GENE...")
for g in GENES:
    print(f"GENE {g}")
    response = c.talk(f"GENE {g}")
    print(f"{response}\n")
