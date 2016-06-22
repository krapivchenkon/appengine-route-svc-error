import webapp2
import logging
import os


class Hello(webapp2.RequestHandler):
    def get(self):
      
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            ENV="PROD"
        else:
            ENV="DEV_APPSERVER"
        self.response.write('Hello, world from Python MAIN:'+ENV+'\n')

application = webapp2.WSGIApplication([
    # In order to make dispatch.yaml work, we handle /.*, so /py/*
    # is served by Hello handler.
    ('/.*', Hello)
], debug=True)
