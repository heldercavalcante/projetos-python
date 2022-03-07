from random import randint

produtos = [
    {'id': 1,
     'nome': 'Tv',
     'preço': 1456.33,
     'qtd_estoque': 10,
     'ativo': True},
    {'id': 2,
     'nome': 'Sofá',
     'preço': 480.43,
     'qtd_estoque': 6,
     'ativo': True},
    {'id': 3,
     'nome': 'Celular',
     'preço': 1899.99,
     'qtd_estoque': 30,
     'ativo': True},
    {'id': 4,
     'nome': 'Notebook',
     'preço': 4300.00,
     'qtd_estoque': 0,
     'ativo': False},
]


def imprimir_produtos_disponiveis():
    print('\nLista de Produtos disponiveis:')
    for produto in produtos:
        if produto['qtd_estoque'] > 0 and produto['ativo'] == True:
            print(f"\t{produto['id']}- {produto['nome']} R${produto['preço']} ({produto['qtd_estoque']}"
                  f" itens em estoque)")
            id_produtos_disponiveis.append(produto['id'])


def verificar_se_id_escolhido_esta_disponivel():
    while True:
        id_produto_escolhido = input('digite o ID do produto que você deseja adicionar ao carrinho: ')
        if id_produto_escolhido.isnumeric():
            id_produto_escolhido = int(id_produto_escolhido)
            if id_produto_escolhido in id_produtos_disponiveis:
                print('\nProduto adicionado ao carrinho com sucesso!\n')
                break
            else:
                print('\nO produto escolhido esta inativo ou sem estoque!!!\n')
        else:
            print('\nO ID digitado não é um numero!!!\n')
    return id_produto_escolhido


def add_produto_ao_carrinho():
    for produto in produtos:
        if id_escolhido == produto['id']:
            carrinho.append({'id_produto': produto['id'], 'descrição': produto['nome'], 'quantidade': 1,
                             'valor_unitario': produto['preço']})
            id_itens_carrinho.append(produto['id'])


def imprimir_produtos_do_carrinho(pedido):
    print(f'\nProdutos do {pedido}: ')
    valor_total = 0
    for produto_add in carrinho:
        print(f"\t(id:{produto_add['id_produto']}) {produto_add['quantidade']}x - {produto_add['descrição']} un: R$ {produto_add['valor_unitario']} total:"
              f" R$ {produto_add['valor_unitario'] * produto_add['quantidade']}")
        valor_total += produto_add['valor_unitario']* produto_add['quantidade']
    print(f'Valor total é igual a: R$ {round(valor_total,2)}')


def pegar_posicao_no_carrinho():
    posicao = 0
    for produto in carrinho:
        if id_escolhido == produto['id_produto']:
            return posicao
        posicao += 1
    raise Exception('Produto não encontrado')


def verificar_se_item_esta_no_carrinho():
    while True:
        item_escolhido = input('\nDigite o ID do produto escolhido: ')
        if item_escolhido.isnumeric():
            item_escolhido = int(item_escolhido)
            if item_escolhido in id_itens_carrinho:
                print()
                break
            else:
                print('\nO produto escolhido não esta no carrinho!!!\n')
        else:
            print('\nO ID digitado não é um numero!!!\n')
    return item_escolhido


def nova_quantidade_escolhida():
    while True:
        nova_quantidade = input('Qual a nova quantidade você quer colocar nesse item? ')
        if nova_quantidade.isnumeric():
            nova_quantidade = int(nova_quantidade)
            if nova_quantidade > 0:
                for produto in produtos:
                    if item_alterar == produto['id']:
                        if nova_quantidade <= produto['qtd_estoque']:
                            return nova_quantidade
                        else:
                            print('\nQuantidade indisponivel no estoque!!!\n')
            else:
                print('\nA quantidade não pode ser menor ou igual a 0 !!!\n')
        else:
            print('\nO item digitado não é um numero valido!!!\n')


id_produtos_disponiveis = []
id_itens_carrinho = []
carrinho = []
rota = 'pagina_inicial'

while True:
    if rota == 'pagina_inicial':
        print('\nBem vindo ao Magazine das Ofertas\n')
        rota = 'lista_de_produtos'
        continue
    if rota == 'lista_de_produtos':
        imprimir_produtos_disponiveis()
        id_escolhido = verificar_se_id_escolhido_esta_disponivel()
        try:
            posicao = pegar_posicao_no_carrinho()
            carrinho[posicao]['quantidade'] += 1
        except:
            add_produto_ao_carrinho()
        rota = 'carrinho'
        continue
    if rota == 'carrinho':
        imprimir_produtos_do_carrinho('carrinho')
        print('\nEscolha o que deseja fazer:\n1- Escolher outro produto para Adicionar no carrinho\n'
              '2- Alterar quantidade de um produto no carrinho\n3- Deletar um produto do carrinho\n'
              '4- Finalizar Pedido')
        nova_acao = input('Digite o numero conrrespondente a ação: ')
        if nova_acao.isnumeric():
            nova_acao = int(nova_acao)
            if nova_acao == 1:
                rota = 'lista_de_produtos'
                continue
            elif nova_acao == 2:
                imprimir_produtos_do_carrinho('carrinho')
                item_alterar = verificar_se_item_esta_no_carrinho()
                id_escolhido = item_alterar
                index = pegar_posicao_no_carrinho()
                nova_quantidade = nova_quantidade_escolhida()
                carrinho[index]['quantidade'] = nova_quantidade
                rota = 'carrinho'
                continue
            elif nova_acao == 3:
                imprimir_produtos_do_carrinho('carrinho')
                item_deletar = verificar_se_item_esta_no_carrinho()
                id_escolhido = item_deletar
                index = pegar_posicao_no_carrinho()
                del carrinho[index]
                rota = 'carrinho'

            elif nova_acao == 4:
                numero_pedido = randint(1, 100)
                print(f'\nO pedido de n°{numero_pedido} foi finalizado com sucesso!')
                imprimir_produtos_do_carrinho('pedido')
                break
            else:
                print('\nNumero digitado não corresponde as opções disponiveis!!!\n')
        else:
            print('\nVocê tem que digitar um numero!!!\n')
