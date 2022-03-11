class Product:

    def __init__(self, id, name, price, stock, active):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.active = active

    def has_stock(self):
        return self.stock > 0

    def is_active(self):
        if self.active:
            return True
