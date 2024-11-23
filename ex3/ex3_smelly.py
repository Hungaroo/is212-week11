class products:
    def __init__(self,name,price,discount_rate,tax_rate):
        self.name = name
        self.price = price
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
    
    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate)
        print(f"Discounted price for {self.name} ({self.__class__.__name__}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} ({self.__class__.__name__}): {tax}")
        return tax

class Electronics:
    def __init__(self, name, price,discount_rate,tax_rate):
        self.name = name
        self.price = price
        self.discount_rate = 0.10
        self.tax_rate = 0.15

class Clothing:
    def __init__(self, name, price,discount_rate,tax_rate):
        self.name = name
        self.price = price
        self.discount_rate = 0.20
        self.tax_rate = 0.08

class Grocery:
    def __init__(self, name, price,discount_rate,tax_rate):
        self.name = name
        self.price = price
        self.discount_rate = 0.05
        self.tax_rate = 0.02