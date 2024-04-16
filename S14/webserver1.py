import http.server  # provides tools that allow to be able to easily program a http server
import socketserver  # provides tools that simplifies the tasks of creating and managing the server socket

# Define the Server's port, AND ONLY THE PORT since the IP is to be taken as the local one by default
PORT = 8080


# -- This is for preventing the error: "Port already in use", works like:
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) , but now we put it in a better way
socketserver.TCPServer.allow_reuse_address = True
# equal to True means we are reusing the socketserver


# -- Use the http.server Handler
handler = http.server.SimpleHTTPRequestHandler  # = simple http request handler
# stores the CLASS whose object will be in charge of handling the http requests received by the server and can respond
# will only process http received from clients to the server, but ONLY performs SIMPLE functions


# -- Open the socket server (creates the server socket, does a bind and creates an object to handle http requests)
with socketserver.TCPServer(("", PORT), handler) as httpd:  # d states for "Demon": process never ends
    # "with" creates a CONTEXT, and with "as" we introduce the VARIABLE: simplifies client management part of process
    # socketserver is a module, TCPServer is a class, and we put () to call the init of this class TO CREATE AN OBJECT
    # we pass to this constructor the server_address and the handler(object) that accepts the conexions & process http

    # NOW THIS IS EXECUTED:
    print(f"Serving at PORT {PORT}")

    # -- Main loop: Attend the client. Whenever there is a new clint, the handler is called
    try:
        httpd.serve_forever()  # would act as a while true (INFINITE LOOP), accept, processing and closing of connexion
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()
