class CartPage:

    def __init__(self):
        self.components = []

    def add_cart_product(self, component):
        self.components.append(component)

    def have_this_product(self, id_chose):
        for componet in self.components:
            if componet.id_product == id_chose:
                return True
        return False

    def show_products_in_cart(self):
        print('\nProdutos do Carrinho:')
        total = 0
        for component in self.components:
            print(f'\t(ID: {component.id_product}) {component.quantity}x - {component.description}'
                  f' un: R${component.unitary_value} '
                  f'total: R${round(component.unitary_value*component.quantity,2)}'.replace('.', ','))
            total += component.unitary_value * component.quantity
        print(f'Valor total é igual a: R${round(total,2)}'.replace('.', ','))

    def increase_quantity(self, id_chose):
        for component in self.components:
            if component.id_product == id_chose:
                component.quantity += 1

    def change_quantity(self, id_chose, new_quantity):
        for component in self.components:
            if component.id_product == id_chose:
                component.quantity = new_quantity

    def del_product(self, product):
        self.components.remove(product)

    def get_cart_product_by_id(self, id_chose):
        for component in self.components:
            if id_chose == component.id_product:
                return component
        raise Exception('Aconteceu um erro inesperado')
