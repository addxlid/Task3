import http.server
import socketserver
from typing import Dict, List
from urllib.parse import parse_qs
from urllib.parse import urlparse


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        id = ''
        unid_server = ''
        mes = ''
        err = 'Error'
        query_components: dict[str, list[str]] = parse_qs(urlparse(self.path).query)

        if 'id' in query_components:
            id: str = str(query_components["id"][0])
        if 'unid_server' in query_components:
            unid_server = str(query_components["unid_server"][0])
        if 'mes' in query_components:
            mes = str(query_components["mes"][0])
            tofind = str(id + unid_server+"\n")
            with open('clients.txt') as f:
                if tofind in f:
                    err = 'Done'
                    f = open("Logfile.txt", 'a')
                    f.write(mes + "\n")
                    f.close()

        html = f'<html><head></head><body><h1>{err}</h1></body></html>'

        self.wfile.write(bytes(html, "utf8"))

        return


handler_object = MyHttpRequestHandler

PORT = 8001
my_server = socketserver.TCPServer(("", PORT), handler_object)

my_server.serve_forever()
