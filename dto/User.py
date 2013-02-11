from google.appengine.ext import db
class User(db.Model):
	username = db.StringProperty(required = True)
	password = db.TextProperty(required = True)
	email = db.StringProperty()
	created = db.DateTimeProperty(auto_now_add = True)