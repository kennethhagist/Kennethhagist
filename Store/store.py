from product import Product

class Store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return self

    def del_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        if len(self.products) < 1:
            print "We have no things"
        else:
            for p in self.products:
                p.display_info()

market = Store("Seattle", "Senior Kenneth")
print market.owner
print market.location

candy = Product(.50, "Recess PB cups", .1, "Nestle", .1, "available")
lacriox = Product(1.75, "CranRaspberry", .1, "LaCriox", .1, "available")
candy.display_info()
lacriox.display_info()

market.add_product(candy).add_product(lacriox)
market.inventory()

print "We are no longer stocking candy in our market"
print "%"*50
market.del_product(candy)
market.inventory()