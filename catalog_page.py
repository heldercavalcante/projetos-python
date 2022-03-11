class CatalogPage:

    def __init__(self):
        self.products = []

    def add_products_in_catalog(self, product):
        self.products.append(product)

    def show_catalog(self):
        print('\nProduct Catalog:')
        for product in self.products:
            print(f'\t{product.id}- {product.name} R${product.price} ({product.stock} em estoque)'.replace('.', ','))

    def get_product_by_id(self, id_chose):
        for product in self.products:
            if id_chose == product.id:
                return product
        raise Exception('Aconteceu um erro inesperado')

    def bigger_than_stock(self,id_chose, quantity):
        for product in self.products:
            if product.id == id_chose:
                if quantity > product.stock:
                    return True
        return False
