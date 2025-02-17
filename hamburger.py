class Hamburger:
    def __init__(self):
        self.ingredients = []

    def add_bun(self, bun):
        self.ingredients.append("Bun: " + bun)

    def add_vegetables(self, vegetables):
        self.ingredients.append("Vegetables: " + vegetables)

    def add_main(self, main):
        self.ingredients.append("Main: " + main)

    def add_sauce(self, sauce):
        self.ingredients.append("Sauce: " + sauce)

    def add_hot_addition(self, hot_addition):
        self.ingredients.append("Hot Addition: " + hot_addition)

    def add_packaging(self, packaging):
        self.ingredients.append("Packaging: " + packaging)

    def add_price(self, price):
        self.ingredients.append("Price: " + price)

    def __str__(self):
        return "Hamburger with: " + ", ".join(self.ingredients)
