import webapp2
from FrontPage import FrontPage
from SignUp import SignUpPage
from LogIn import LoginPage
from LogIn import LogoutPage
from ListIngredientsPage import ListIngredientsPage


app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/signup', SignUpPage),
    ('/login', LoginPage),
    ('/logout', LogoutPage),
    ('/ingredient_list', ListIngredientsPage)
], debug=True)
