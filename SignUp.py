from Handler import Handler
from User import *
from Utilities import valid_username
from Utilities import valid_password
from Utilities import valid_email
from Utilities import pw_hash

class SignUpPage(Handler):
	
	def get(self):
		cookie_username = self.request.cookies.get('user_id')
		if(cookie_username and valid_username(cookie_username)):
			self.redirect('/')
		else:
			self.render('signup-form.html')	

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")
		has_error = False
		params = dict(username = username, email=email)
		if not valid_username(username):
			params['error_username'] = "That's not a valid username."
			has_error = True
		if not valid_password(password):
			params['error_password'] = "That's not a valid password."
			has_error = True
		if not (password == verify):		
			has_error = True
			params['error_verify'] = "Your passwords didn't match."
		if email:
			if not valid_email(email):
				params['error_email'] = "That's not a valid email."
				has_error = True

		if has_error:
			self.render('signup-form.html', **params)
		else:
			users = getByUsername(username)
			if users.count() != 0:
				params['error_user'] = "That user already exists"
				self.render('signup-form.html', **params)
			else:
				hash_password = pw_hash(password)
				u = User(username=username,password=hash_password,email=email)
				u.put()
				self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/'%str(username))
				self.redirect('/')