import http.server
import socketserver

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):  # TestHandler is a daughter class of BaseHTTP
    def do_GET(self):  # for every resource you request from the server this code will be executed. IT DOESN'T ANSWER
        """This method is called whenever the client invokes the GET method/request in the HTTP protocol request"""

        # We just print a message
        print("GET received!")

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler  # stores the CLASS whose object will be in charge of handling the http requests

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
