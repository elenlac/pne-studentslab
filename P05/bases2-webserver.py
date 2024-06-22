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
        # PREDEFINED RESOURCES ONLY:
        resource_to_file = {  # could act as a "constant" or a static class attribute (TestHandler.resource_to_file)
            "/": "basic_index.html",
            "/basic_index.html": "basic_index.html",
            "/info/A.html": os.path.join("info", "A.html"),
            "/info/C.html": os.path.join("info", "C.html"),
            "/info/G.html": os.path.join("info", "G.html"),
            "/info/T.html": os.path.join("info", "T.html")
        }
        filename = resource_to_file.get(resource, resource[1:])  # if the key doesn't exist, we have a default value(dv)
        # when it is not in the dictionary it will do: _other.html -> other.html
        # when defined in the dictionary it will do: /info/A.html -> info/A.html (key-value pair) it won't go to the dv
        filepath = os.path.join("html", filename)
        # when it is not in the dictionary it will do: other.html -> html/other.html (where we are asked to search)
        # when defined in the dictionary it will do: info/A.html -> html/info/A.html

        try:
            contents = Path(filepath).read_text()  # create object with Path class and will read the content of file
            self.send_response(200)  # it will be executed if the previous line is correct
        except FileNotFoundError:  # but if the file does not exist the exception is thrown
            filepath = os.path.join("html", "error.html")
            contents = Path(filepath).read_text()
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
