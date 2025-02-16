class Shoppingcart:
    def __init__(self,items,total_cost):
        self.items = []
        self.total_cost = 0
    def add_items(self,items):
        self.items.append(items)
        self.total_cost += items.price
        print(f"{items.name},(${items.price}) is added to cart. Total cost is now ${self.total_cost}")
    def remove_items(self,items):
        self.items.remove(items)
        self.total_cost -= items.price
        print(f"{items.name},(${items.price}) is removed from cart. Total cost is now ${self.total_cost}")
    def empty_cart(self):
        self.items = []
        self.total_cost = 0
        print("cart is empty")
    def print_cart_info(self):
        print(f"the total cost is{self.total_cost}")
        for item in self.items:
            print(f"{item.name} - ${item.price}")
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
my_shoppingcart = Shoppingcart([],0)
my_1items = Item(name="cheese",price=5)
my_2items = Item(name="tissue paper",price=10)
my_3items = Item(name="chocolate",price=3)
my_shoppingcart.add_items(my_1items)
my_shoppingcart.add_items(my_2items)
my_shoppingcart.add_items(my_3items)
my_shoppingcart.remove_items(my_2items)
my_shoppingcart.empty_cart()
my_shoppingcart.print_cart_info()




