import webapp2
from FrontPage import FrontPage
from SignUp import SignUpPage


app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/signup', SignUpPage)
], debug=True)
