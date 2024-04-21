import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying that everything is ok

        # Message to send back to the client from the server. NOW IT SENDS A RESPONSE!!!!
        body = "I am the happy server! :-)"

        # Generating the response message. METHOD since there is a (), INHERITED from BaseHTTP that I can use directly
        self.send_response(200)
        # -- ESTABLISHES HTTP CODE OF THE RESPONSE = Status line: OK! (internally generates the code-message associated)

        # Define the content-type and content-length header. ANOTHER METHOD, called twice
        self.send_header('Content-Type', 'text/plain')  # key-value
        self.send_header('Content-Length', len(body.encode()))  # transform string to bytes and count them

        # The header is finished, to stop constructing headers it adds a blank line to separate the header from the body
        self.end_headers()

        # Send the response message: takes the response, encodes to bytes and sends the bytes through the client socket
        self.wfile.write(body.encode())  # write file: output path from server to client

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
