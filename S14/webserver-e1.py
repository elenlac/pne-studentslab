import http.server
import socketserver
import termcolor

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        contents = "Resource not available"  # we establish this predefined value
        if self.path == "/":
            contents = "Welcome to my server"  # we change the value
            self.send_response(200)
        else:  # we don't need to establish the value of contents here again since it has already been set before
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', str(len(contents_bytes)))  # the key-value expects to receive two str
        self.end_headers()

        self.wfile.write(contents_bytes)

        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT...", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
