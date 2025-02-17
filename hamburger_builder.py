from abc import ABC, abstractmethod
from hamburger import Hamburger

class HamburgerBuilder(ABC):
    def __init__(self):
        self._hamburger = None

    def get_hamburger(self):
        return self._hamburger

    def build_hamburger(self):
        self._hamburger = Hamburger()
        self.add_bun()
        self.add_vegetables()
        self.add_main()
        self.add_sauce()
        self.add_hot_addition()
        self.add_packaging()
        self.add_price()
        return self

    @abstractmethod
    def add_bun(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def add_main(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_hot_addition(self):
        pass

    @abstractmethod
    def add_packaging(self):
        pass

    @abstractmethod
    def add_price(self):
        pass
