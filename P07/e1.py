import http.client
import json
from http import HTTPStatus

SERVER = 'rest.ensembl.org'  # domain/address of ensembl server, translates to an IP
RESOURCE = '/info/ping'
PARAMS = '?content-type=application/json'  # we state the type of format we want our info to be in
URL = SERVER + RESOURCE + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)  # the PORT used is the 80 (default html port)

try:
    conn.request("GET", RESOURCE + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    data = json.loads(data_str)
    print(data)  # {'ping': 1}
    ping = data['ping']  # we store in this variable the value associated to the key "ping"
    if ping == 1:
        print("PING OK! The database is running!")
    else:
        print("...")
