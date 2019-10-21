import http.server
import json
from urllib.parse import parse_qs
from resistor import decodeResistance

class Service(http.server.BaseHTTPRequestHandler):
    
    #Gets the url path from the request and parses the resource.
    #Takes the resource and checks if valid, if so it returns a 
    # formatted resistance output based on the bands inserted.
    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            [resource, queryString] = self.path.split('?')
            self.log_message("resource: %s", resource)
            self.log_message("query string: %s", queryString)
            
            if 'decode' not in resource:
                self.log_message("decoded not in " + resource)
                self.send_error(404)
                
            bands = parse_qs(queryString)
            self.log_message("built bands... qs = %s", str(bands))
            bandsList = self.formResistanceBandsList(bands)
            self.log_message("built bandsList...")
            
            decoded = decodeResistance(bandsList)
            self.log_message("resistance decoded...")
            body = self.buildResponseBody(decoded)
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))
            
        except Exception as e:
            
            self.send_error(400, str(e))

    #Forms the list of resistance bands based on the given dictionary.
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

    #Returns a basic html format with the given resistance as an h1 tag.
    def buildResponseBody(self, decodedJson):
        resistance = decodedJson['formatted']
        return f"""
        <html>
            <head>
                <title>Resistance</title>
            </head>
            <body>
                <h1 id='resistance_output'>{resistance}</h1>
            </body>
        </html>
        """

if __name__ == "__main__":
    # start the server
    print("Resistance-decoding webserver running on port 8000")
    daemon = http.server.HTTPServer(('', 8000), Service)
    daemon.serve_forever()
