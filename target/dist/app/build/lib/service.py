import http.server
import json
from urllib.parse import parse_qs
from resistor import decodeResistance

class Service(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            [resource, queryString] = self.path.split('?')
            self.log_message("resource: %s", resource)
            self.log_message("query string: %s", queryString)
            
            if resource != 'decode':
                self.log_message("resource: " + resource)
                self.send_error(404)
                
            bands = parse_qs(queryString)
            self.log_message("built bands... qs = %s", str(bands))
            bandsList = self.formResistanceBandsList(bands)
            self.log_message("built bandsList...")
            
            decoded = decodeResistance(bandsList)
            body = self.buildResponseBody(decoded)
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.wrap(bytes(body, 'UTF-8'))
            
        except Exception as e:
            self.send_error(400, str(e))


    def formResistanceBandsList(self, bandsDictionary):
        if len(bandsDictionary) == 4:
            return [
                bandsDictionary['band1'][0],
                bandsDictionary['band2'][0],
                bandsDictionary['band3'][0],
                bandsDictionary['band4'][0]
            ]
        elif len(bandsDictionary) == 5:
            return [
                bandsDictionary['band1'][0],
                bandsDictionary['band2'][0],
                bandsDictionary['band3'][0],
                bandsDictionary['band4'][0],
                bandsDictionary['band5'][0]
            ]
        else:
            raise Exception()


    def buildResponseBody(self, decodedJson):
        resistance = decodedJson['formatted']
        return "test"


# start the server
print("Resistance-decoding webserver running on port 8000")
daemon = http.server.HTTPServer(('', 8000), Service)
daemon.serve_forever()
