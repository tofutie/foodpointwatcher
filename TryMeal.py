from Handler import Handler

class TryMealPage(Handler):
    COUNT = 0
    def get(self):
        self.render('try_meal.html', count=self.COUNT)
    
    def post(self):
        count = int(self.request.get("count"))
        self.write(str(count))
        self.write("<br />")
        ingredients = []
        for i in range(0,count):
            ingredients.append(self.request.get("ingredient%s"%i))
            self.write(ingredients[i])
            self.write("<br />")
            