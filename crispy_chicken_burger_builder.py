from hamburger_builder import HamburgerBuilder


class CrispyChickenBurgerBuilder(HamburgerBuilder):
    def add_bun(self):
        self._hamburger.add_bun("Toasted sesame bun")

    def add_vegetables(self):
        self._hamburger.add_vegetables("Lettuce, tomato, and pickles")

    def add_main(self):
        self._hamburger.add_main("Crispy Chicken fillet")

    def add_sauce(self):
        self._hamburger.add_sauce("Spicy mayo")

    def add_hot_addition(self):
        self._hamburger.add_hot_addition("Fries")

    def add_packaging(self):
        self._hamburger.add_packaging("Paper wrap")

    def add_price(self):
        self._hamburger.add_price("39.90")
