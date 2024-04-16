import http.server
import socketserver
import termcolor
from pathlib import Path
import os

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        resource = self.path

        if resource == "/" or resource == "/index.html":
            filename = os.path.join("html", "index.html")  # since it is in the directory "html" we first build the path
            contents = Path(filename).read_text()
            self.send_response(200)
        elif resource == "/info/A.html":
            filename = os.path.join("html","info","A.html")
            contents = Path(filename).read_text()
            self.send_response(200)
        elif resource == "/info/C.html":
            filename = os.path.join("html","info","C.html")
            contents = Path(filename).read_text()
            self.send_response(200)
        elif resource == "/info/G.html":
            filename = os.path.join("html","info","G.html")
            contents = Path(filename).read_text()
            self.send_response(200)
        elif resource == "/info/T.html":
            filename = os.path.join("html","info","T.html")
            contents = Path(filename).read_text()
            self.send_response(200)
        else:  # client has asked for other web page different from the predefined ones
            web_page = self.path[1:]  # we create a substring, deleting the "/" from the path line
            try:
                filename = os.path.join("html", web_page)  # if requested web page exists, has to be in that directory
                contents = Path(filename).read_text()  # create object with Path class and will read the content of file
                self.send_response(200)  # it will be executed if the previous line is correct
            except FileNotFoundError:  # but if the file does not exist the exception is thrown
                filename = os.path.join("html", "error.html")
                contents = Path(filename).read_text()
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
