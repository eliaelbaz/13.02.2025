from hamburger_builder import HamburgerBuilder


class BeyondBurgerBuilder(HamburgerBuilder):
    def add_bun(self):
        self._hamburger.add_bun("Whole grain bun")

    def add_vegetables(self):
        self._hamburger.add_vegetables("Mixed greens and red onion")

    def add_main(self):
        self._hamburger.add_main("Beyond meat patty")

    def add_sauce(self):
        self._hamburger.add_sauce("Vegan BBQ sauce")

    def add_hot_addition(self):
        self._hamburger.add_hot_addition("Sweet potato fries")

    def add_packaging(self):
        self._hamburger.add_packaging("Eco-friendly packaging")

    def add_price(self):
        self._hamburger.add_price("49.90")
