from google.appengine.ext import db

class Ingredient(db.Model):
	name = db.StringProperty(required = True)
	base_amount = db.FloatProperty(required = True)
	unit = db.StringProperty(required = True)
	base_points = db.IntegerProperty(required = True)
	createdby = db.StringProperty()
	
def getIngredientByName(name):
	return db.GqlQuery("SELECT * FROM Ingredient WHERE name='%s'"%name)

def getAllIngredients():
	return db.GqlQuery("SELECT * FROM Ingredient ORDER BY name ASC")