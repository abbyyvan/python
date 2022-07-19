class CoffeeMaker:
    def __init__(self):
        self.resoures = {
            "water":300,
            "milk" 200,
            "coffee":100,
        }

    def report(self):

        print(f"")

    def is_resource_sufficient(self):
        return booleans(self)

    def make_coffee(self,order):

        print(f"Here's your {order.name}, Enjoy!")