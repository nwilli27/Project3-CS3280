import http.server


class Service(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            if resource not in "resistance.html":
                self.log_message("resource: " + path)
                self.send_error(404)
            body = self.buildResponseBody(resource)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))
        except Exception as e:
            self.send_error(400, str(e))



    def buildResponseBody(self, filename):
        infile = open(filename)
        body = infile.read()
        infile.close()
        return body

# start the server
print("webserver running on port 8000")
daemon = http.server.HTTPServer(('', 8000), Service)
daemon.serve_forever()
