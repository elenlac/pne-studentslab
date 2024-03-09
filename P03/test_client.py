from Client3 import Client

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

c = Client(SERVER_IP, SERVER_PORT)
print(f"Connection to SERVER at {SERVER_IP}, PORT: {SERVER_PORT}")

print(f"* Testing PING...")
response = c.talk("PING")
print(f"{response}\n")

print(f"* Testing GET...")
for n in range(5):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response}")
print(f"\n")

print(f"* Testing INFO...")
response = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"{response}\n")

print(f"* Testing COMP...")
response = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"{response}\n")

print(f"* Testing REV...")
response = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"{response}\n")

print(f"* Testing GENE...")
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for g in GENES:
    response = c.talk(f"GENE {g}")
    print(f"GET {g}: {response}")
print(f"{response}\n")
