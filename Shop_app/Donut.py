class Donut:
    def __init__(self, flavor, quantity):
        self._flavor = flavor
        self._quantity = quantity

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
            self._quantity = quantity
