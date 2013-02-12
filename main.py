import webapp2
from FrontPage import FrontPage
from SignUp import SignUpPage
from LogIn import LoginPage
from LogIn import LogoutPage
from ListIngredientsPage import ListIngredientsPage
from ListIngredientsPage import EditIngredientPage


app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/signup', SignUpPage),
    ('/login', LoginPage),
    ('/logout', LogoutPage),
    ('/ingredient_list', ListIngredientsPage),
    ('/ingredient', EditIngredientPage)
], debug=True)
