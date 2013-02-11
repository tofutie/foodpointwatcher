from Handler import Handler
from User import *
from Utilities import pw_hash
from Utilities import valid_username
class LoginPage(Handler):
	def get(self):
		cookie_username = self.request.cookies.get('user_id')
		if(cookie_username and valid_username(cookie_username)):
			self.redirect('/')
		else:
			self.render('login-form.html')

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		has_error = False
		params = dict()
		if not valid_username(username):
			params['error_username'] = "That's not a valid username."
			has_error = True
		else:
			users = getByUsername(username)	
			if users.count() != 0:
				p_hash = users[0].password
				salt = p_hash.split(',')[1]
				hashy = pw_hash(password,salt)
				if hashy.split(',')[0] == p_hash.split(',')[0]:
					#set cookie and redirect!
					self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/'%str(username))
					self.redirect('/')
				else:
					has_error = True
					params['error_password'] = "Your password or username is incorrect"
			else:
				has_error = True
				params['error_exists'] = "That user does not exist<br /><a href='/signup'>Click here to Signup</a>"

		if has_error:
			self.render('login-form.html', **params)
                        
class LogoutPage(Handler):
	def get(self):
		self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
		self.redirect('/')