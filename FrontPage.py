from Handler import Handler

class FrontPage(Handler):
    def get(self):
        self.render('front.html')