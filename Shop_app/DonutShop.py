class DonutShop:
    def __init__(self):
        self._inventory = []

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        self._inventory = inventory

    def add_donut(self, donut):
        for existing_donut in self._inventory:
            if existing_donut.flavor == donut.flavor:
                existing_donut.quantity += donut.quantity
                break
        else:
            self._inventory.append(donut)

    def get_inventory(self):
        return self._inventory