import webapp2
from FrontPage import FrontPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2 world!')

app = webapp2.WSGIApplication([
    ('/', FrontPage)
], debug=True)
