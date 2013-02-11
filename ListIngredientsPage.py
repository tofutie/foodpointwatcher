from Handler import Handler
from Ingredient import *
from fractions import Fraction

class ListIngredientsPage(Handler):
	def render_list(self, name="", base_amount="", unit="", base_points="", error=""):
		ingredients = getAllIngredients()
		self.render("food_list.html", ingredients=ingredients,name=name, amount=base_amount, unit=unit, points=base_points, error=error)
	def get(self):
		self.render_list()
	def post(self):
		name = self.request.get("name")
		base_amount = self.request.get("amount")
		unit = self.request.get("unit")
		base_points = self.request.get("points")
		
		params = dict()

		if name and base_amount and unit and base_points:
			i = Ingredient(name=name, base_amount=round(float(sum(Fraction(s) for s in base_amount.split())),2), unit=unit, base_points = int(base_points))
			i.put()
			self.redirect("/ingredient_list")
		else:
			error = "All fields must be filled out."
			params['error'] = error
			self.render_list(name, base_amount, unit, base_points, error)