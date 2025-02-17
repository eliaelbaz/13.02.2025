from hamburger_builder import HamburgerBuilder


class HomeBurgerBuilder(HamburgerBuilder):
    def add_bun(self):
        self._hamburger.add_bun("Classic bun")

    def add_vegetables(self):
        self._hamburger.add_vegetables("Fresh lettuce and tomato")

    def add_main(self):
        self._hamburger.add_main("Mixed beef patty")

    def add_sauce(self):
        self._hamburger.add_sauce("House special sauce")

    def add_hot_addition(self):
        self._hamburger.add_hot_addition("Salad")

    def add_packaging(self):
        self._hamburger.add_packaging("Standard box")

    def add_price(self):
        self._hamburger.add_price("29.90")
