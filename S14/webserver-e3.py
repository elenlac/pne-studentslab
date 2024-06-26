import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/" or self.path == "/basic_index.html":
            contents = Path("index.html").read_text()
            self.send_response(200)
        else:
            resource = self.path[1:]  # we create a substring, deleting the "/" from the path line
            try:
                contents = Path(resource).read_text()  # create object with Path class and will read the content of file
                self.send_response(200)  # it will be executed if the previous line is correct
            except FileNotFoundError:  # but if the file does not exist the exception is thrown
                contents = Path("error.html").read_text()
                self.send_response(404)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
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
