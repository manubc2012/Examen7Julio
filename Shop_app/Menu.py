from Shop_app.Donut import Donut


class Menu:
    def __init__(self, shop):
        self.shop = shop

    def run(self):
        while True:
            print("\n1. Agregar sabor de dona")
            print("2. Mostrar inventario")
            print("3. Salir")
            option = input("Elige una opción: ")
            if option == "1":
                flavor = input("Ingresa el sabor de la dona: ")
                quantity = int(input("Ingresa la cantidad de donas: "))
                donut = Donut(flavor, quantity)
                self.shop.add_donut(donut)
            elif option == "2":
                inventory = self.shop.get_inventory()
                for donut in inventory:
                    print(f"Sabor: {donut.flavor}, Cantidad: {donut.quantity}")
            elif option == "3":
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")