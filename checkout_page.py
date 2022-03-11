class CheckoutPage:

    def __init__(self, products):
        self.request = products

    def print_final_request(self, number):
        total = 0
        print(f'\nPedido de n°{number} foi finalizado com sucesso!\n')
        print('Produtos do seu pedido:')
        for item in self.request:
            print(f'\t{item.quantity}x - {item.description}'
                  f' un: R${item.unitary_value} '
                  f'total: R${round(item.unitary_value * item.quantity, 2)}'.replace('.', ','))
            total += item.unitary_value * item.quantity
        print(f'Valor total do pedido: R${round(total, 2)}'.replace('.', ','))

