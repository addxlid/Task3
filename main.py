import http.server
import socketserver
import uuid
from urllib.parse import parse_qs
from urllib.parse import urlparse


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        unid = ''
        unid_server = ''
        query_components = parse_qs(urlparse(self.path).query)
        if 'unid' in query_components:
            unid = str(query_components["unid"][0])
            unid_server = str(uuid.uuid4())
            f = open("clients.txt", 'a')
            f.write(unid + unid_server + "\n")
            f.close()

        html = f"<html><head></head><body><h1>Hello {unid}</h1></br><h2>Your code: {unid_server}</h2></body></html>"

        self.wfile.write(bytes(html, "utf8"))

        return


handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

my_server.serve_forever()
