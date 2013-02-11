from Handler import Handler
from Utilities import valid_username

class FrontPage(Handler):
    def get(self):
        cookie_username = self.request.cookies.get('user_id')
        if(cookie_username and valid_username(cookie_username)):
            self.render('front.html', username=cookie_username)
        else:
            self.render('front.html')