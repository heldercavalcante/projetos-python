from product import Product
from home_page import HomePage
from catalog_page import CatalogPage
from cart import CartComponets
from cart_page import CartPage
from checkout_page import CheckoutPage
from random import randint

# DEFINING OBJECTS
home_page = HomePage('magazine das ofertas!')
catalog = CatalogPage()
catalog.add_products_in_catalog(Product(1, 'Tv smart', 1456.33, 10, True))
catalog.add_products_in_catalog(Product(2, 'Sofá familia', 1230.43, 6, True))
catalog.add_products_in_catalog(Product(3, 'Galaxy S10', 1899.99, 30, True))
catalog.add_products_in_catalog(Product(4, 'Cama para casal', 1090.22, 52, True))
catalog.add_products_in_catalog(Product(5, 'Notebook', 4200.23, 100, True))
cart = CartPage()
checkout = CheckoutPage(cart.components)


# FUNCTIONS
def catalog_page():
    catalog.show_catalog()
    while True:
        id_chose = input('Digite o ID do produto que quer adicionar ao carrinho: ')
        if id_chose.isnumeric():
            id_chose = int(id_chose)
            if id_chose <= len(catalog.products):
                if catalog.products[id_chose-1].has_stock() and catalog.products[id_chose-1].is_active():
                    break
                else:
                    print('\nO produto correspondente ao ID digitado está sem estoque ou inativo!!!\n')
            else:
                print('\nO ID digitado não pertence a lista de produtos do catalogo!!!\n')
        else:
            print('\nVocê tem que digitar um numero!!!\n')
    print('\nProduto adicionado ao carrinho!!!')
    if cart.have_this_product(id_chose):
        cart.increase_quantity(id_chose)
    else:
        product_chose = catalog.get_product_by_id(id_chose)
        cart.add_cart_product(CartComponets(product_chose.id, product_chose.name, product_chose.price, 1))


def cart_page():
    cart.show_products_in_cart()
    print('\nEscolha o que deseja fazer:\n1- Escolher outro produto para Adicionar no carrinho\n'
          '2- Alterar quantidade de um produto no carrinho\n3- Deletar um produto do carrinho\n'
          '4- Finalizar Pedido')
    new_action = input('Digite o numero conrrespondente a ação: ')
    if new_action.isnumeric():
        new_action = int(new_action)
        if new_action == 1:
            return 'catalog'
        if new_action == 2:
            while True:
                id_chose = input('\nDigite o ID do produto que você deseja alterar a quantidade: ')
                if id_chose.isnumeric():
                    id_chose = int(id_chose)
                    if cart.have_this_product(id_chose):
                        break
                    else:
                        print('\nNão existe nenhum produto no carrinho com esse ID!!!')
                else:
                    print('\nVocê precisa digitar um numero!!!')
            while True:
                new_quantity = input('Digite a nova quantidade desejada: ')
                if new_quantity.isnumeric():
                    new_quantity = int(new_quantity)
                    if catalog.bigger_than_stock(id_chose, new_quantity):
                        print('\nQuantidade escolhida maior que o estoque disponivel!!!')
                    else:
                        cart.change_quantity(id_chose, new_quantity)
                        break
                else:
                    print('Você precisa digitar um numero!!!')
            return 'cart'
        if new_action == 3:
            id_chose = int(input('\nDigite o ID do produto que você deseja deletar: '))
            product_chose = cart.get_cart_product_by_id(id_chose)
            cart.del_product(product_chose)
            return 'cart'
        if new_action == 4:
            return 'checkout'
        else:
            print('\nNumero digitado não corresponde as opções disponiveis!!!\n')
            return 'cart'
    else:
        print('\nVocê precisa digitar um numero!!!\n')
        return 'cart'


def checkout_page():
    num = randint(1, 100)
    checkout.print_final_request(num)


route = 'homePage'
# SHOPPING LOOP
while True:
    if route == 'homePage':
        home_page.welcome()
        route = 'catalog'
        continue
    if route == 'catalog':
        catalog_page()
        route = 'cart'
        continue
    if route == 'cart':
        route = cart_page()
        continue
    if route == 'checkout':
        checkout_page()
        break
