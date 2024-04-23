import http.server
import socketserver
import termcolor
from pathlib import Path
import os

PORT = 8080
HTML_FOLDER = "html"  # constant that determines the folder where we have all html files

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        filepath = os.path.join(HTML_FOLDER, "form-1.html")
        contents = Path(filepath).read_text()

        self.send_response(200)  # doesn't deal with errors, only OK

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', f"{len(str.encode(contents))}")
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")  # not the same as print()= \n and print("")= empty str that traduces?
        print("Stopped by the user")
        httpd.server_close()
