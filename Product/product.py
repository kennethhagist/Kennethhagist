class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'For sale'

    def Sell(self):
        self.status = "Sold"
        return self

    def Add_tax(self):
        return .089*self.price + self.price
        # return self

    def Reason(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'like new':
            self.status = 'for sale'
        elif reason == 'open box':
            self.status = 'used'
            self.price = .20*self.price
            return self
        else:
            return self

    def display_info(self):
        print 'Price: $' + str(self.price)
        print 'Item Name: ' + self.item_name
        print 'Weight: ' + str(self.weight) + 'oz'
        print 'Brand: ' + self.brand
        print 'Cost: ' + str(self.cost)
        print 'Status: ' + self.status
        return self

product1 = Product(19.99, 'Controller', 5, 'Xbox', 14.99, '')
product2 = Product(12.99, 'Controller', 5, 'Xbox', 14.99, 'open box')
product1.display_info()
product2.Reason('open box')
product2.display_info()
print product1.Sell().Add_tax()
print product2.Sell().Add_tax()
