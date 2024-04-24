# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server without using the web browser (our longstanding client)
import http.client

PORT = 8080
SERVER = 'localhost'  # SERVER = IP

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server: NEW!!!!!!
conn = http.client.HTTPConnection(SERVER, PORT)  # object of class HTTPConnection that builds the cs and connect((,))

# -- Send the request message, using the GET method. We are requesting the main page (/)
try:
    conn.request("GET", "/")
except ConnectionRefusedError:  # if I make a request and the server is not available
    print("ERROR! Cannot connect to the Server")
    exit()  # closes the whole program

"IF THE SERVER KNOWS HOW TO ANSWER"
# -- Read the response message from the server
r1 = conn.getresponse()  # object of class HTTPResponse

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")  # status= code & reason= text associated to code

# -- Read the response's body (REMEMBER ITS OPTIONAL)
data1 = r1.read().decode("utf-8")  # read the bytes of the body received and turns into characters

# -- Print the received data
print(f"CONTENT: {data1}")
