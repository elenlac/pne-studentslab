import http.server
import socketserver
import termcolor
from pathlib import Path
import os
from urllib.parse import urlparse, parse_qs  # library of url module, will help to manage/analyze the requests to server
# and parse is a submodule from which we import two functions (urlparse, parse_qs)
import jinja2 as j  # at the time of referring to jinja2 we establish an alias j


def read_html_file(filename):
    filepath = os.path.join(HTML_FOLDER, filename)  # builds the path to the file
    contents = Path(filepath).read_text()  # object of the class Path that will read the content of the web page given
    contents = j.Template(contents)  # from that module we take the class Template and give the str html file (contents)
    # we are creating an OBJECT that acts as a TEMPLATE that is built as the html code
    return contents


PORT = 8080
HTML_FOLDER = "html"

socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)  # parses/analyzes/slices the route received when the client performs a request
        print(f"URL Path: {url_path}")
        # URL Path: ParseResult(scheme='', netloc='', path='/', params='', query='', fragment='')
        resource = url_path.path  # url path is an object of the class ParseResult that contains attributes like path
        print(f"Path: {resource}")
        arguments = parse_qs(url_path.query)  # this function creates a dictionary with attributes(key-value(list))
        print(f"Arguments: {arguments}")

        if resource == "/":
            filepath = os.path.join(HTML_FOLDER, "form-e1.html")
            contents = Path(filepath).read_text()
            self.send_response(200)
        elif resource == "/echo":  # the client has filled the form and sent it to the server
            try:
                msg_param = arguments['msg'][0]  # obtain the value of "msg" key = list and take the value occupied at 0
                print(msg_param)

                """VERSION 1, in this case it is not in a separated html file since there is a dynamic part"""
                # contents = f"""
                #     <!DOCTYPE html>
                #     <html lang="en">
                #         <head>
                #             <meta charset="utf-8">
                #             <title>Result</title>
                #         </head>
                #         <body>
                #             <h1>Received message:</h1>
                #             <p>{msg_param}</p>  <!-- this is the ONLY dynamic/variable part -->
                #             <a href="/">Main page</a>
                #         </body>
                #     </html>"""

                """VERSION 2"""
                contents = read_html_file("result-echo-server-e1.html").render(context={"todisplay": msg_param})
                # object of type template that contains that html code given
                # we ask him to "refresh"/ "render" (method of class Template)
                # context is a dict which only has a key and a variable value, allows communication of python with html
                self.send_response(200)

            except (KeyError, IndexError):
                filepath = os.path.join(HTML_FOLDER, "error.html")
                contents = Path(filepath).read_text()
                self.send_response(404)
        else:
            filepath = os.path.join(HTML_FOLDER, "error.html")
            contents = Path(filepath).read_text()
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)

        return


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()

