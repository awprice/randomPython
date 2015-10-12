import bottle

# Declaration of new class that inherits from ServerAdapter
# It's almost equal to the supported cherrypy class CherryPyServer
class MySSLCherryPy(bottle.ServerAdapter):
    def run(self, handler):
        from cherrypy import _cpwsgiserver3
        server = _cpwsgiserver3.CherryPyWSGIServer((self.host, self.port), handler)

        # If cert variable is has a valid path, SSL will be used
        # You can set it to None to disable SSL
        server.ssl_certificate = "/path/to/certificate"
        server.ssl_private_key = "/path/to/private/key"
        try:
            server.start()
        finally:
            server.stop()

@bottle.route('/')
def root():
    return "Hello World!"


# Add an additional parameter server='mysslcherrypy' so bottle
# will use our class
bottle.run(host='0.0.0.0', port='8080', server=MySSLCherryPy)
