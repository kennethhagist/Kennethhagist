class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        self.tax = 1.065

    def display_info(self):
        print 'Price: $' + str(self.price)
        print 'Item Name: ' + self.item_name
        print 'Weight: ' + str(self.weight) + 'oz'
        print 'Brand: ' + self.brand
        print 'Cost: ${:,.2f}'.format(self.price * self.tax)
        print 'Status: ' + self.status
        return self

product1 = Product(19.99, 'Controller', 5, 'Xbox', 14.99, '')
product2 = Product(12.99, 'Controller', 5, 'Xbox', 14.99, 'open box')
product1.display_info()
product2.display_info()