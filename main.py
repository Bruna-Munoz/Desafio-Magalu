listProd = {'produto': [], 'preço': []}

while True:
    print(
    """
    ____                                          _                __                
   / __ )  ____   ____ _   _____        _   __   (_)   ____   ____/ /  ____ _   _____
  / __  | / __ \ / __ `/  / ___/ ______| | / /  / /   / __ \ / __  /  / __ `/  / ___/
 / /_/ / / /_/ // /_/ /  (__  ) /_____/| |/ /  / /   / / / // /_/ /  / /_/ /  (__  ) 
/_____/  \____/ \__,_/  /____/         |___/  /_/   /_/ /_/ \__,_/   \__,_/  /____/  
                                                                                 
╠══============================== MENU DE NAVEGAÇÃO =============================══╣

                                    1-Cadastro
                                    2-Vendas 
                                    3-Relatório 
                                    4-Sair 
                              """)
    opcao = input("""
                            INFORME A OPÇÃO DESEJADA: """)
    
    listProd = []
    match opcao:
        case '1':
            print("""
            Menu de Cadastro:​
            a) Cadastrar produtos;
            b) Listar produtos cadastrados;
            c) Deletar produtos;
            d) Voltar ao menu anterior.​
            """)
            opcao_cadastro = input('Escolha uma opção: ').lower()
            while opcao_cadastro == 'a':
                listProd['produto'].append(input('Digite o produto a ser cadastrado: ').lower())
                listProd['preço'].append(float(input('Digite o preço do produto: R$ ').lower()))
                
                novo_prod=input('Deseja cadastrar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()
                if novo_prod == 'n' or novo_prod != 's':
                    break
   
            if opcao_cadastro == 'b':
                print('A lista de produtos cadastrados é:\n',listProd['produto'])

            if opcao_cadastro == 'c':
                pass
            if opcao_cadastro == 'd':
                continue
            while opcao_cadastro not in('a','b','c','d'):
                opcao_cadastro = input('''
                Opção inválida. 
                
                Menu de Cadastro:

                a) Cadastrar produtos;
                b) Listar produtos cadastrados;
                c) Deletar produtos;
                d) Voltar ao menu anterior.

                Escolha uma opção compatível: ''').lower()
                while opcao_cadastro == 'a':
                    listProd['produto'].append(input('Digite o produto a ser cadastrado: ').lower())
                    listProd['preço'].append(float(input('Digite o preço do produto: R$ ').lower()))
                
                    novo_prod=input('Deseja cadastrar mais algum produto? Digite S para "Sim" ou N para "Não": ' ).lower()

                    if novo_prod == 'n' or novo_prod != 's':
                        break

            if opcao_cadastro == 'b':
                print('A lista de produtos cadastrados é:\n',listProd['produto'])

                if opcao_cadastro == 'c':
                    pass
                if opcao_cadastro == 'd':
                    continue
        
        case '2':
            print("""
            Menu de Vendas:
            
            a) Adicionar produtos ao carrinho;
            b) Finalizar a compra;
            c) Voltar ao menu anterior.

            """)
            opcao_venda = input('Escolha uma opção: ').lower()

            valorTotal = 0

            while opcao_venda == 'a':
                print("Produtos disponíveis: ", listProd)

                p = input("Digite o nome do produto sendo comprado: \n")

                while p not in listProd['produto']:
                    print("Produto não cadastrado.")
                    p = input("Digite o nome de um produto válido: \n")

                for p in range(len(listProd['produto'])):
                    for v in range(len(listProd['preço'])):
                        valorTotal += v
                        print("Produto adicionado: ", str(p),
                        "Preço do produto: R$", int(v), 
                        "Valor total da compra: R$", valorTotal)

                    print("""
                    a) Adicionar mais produtos ao carrinho;
                    b) Finalizar a compra.""")
                
                    opcao_venda = input('Escolha uma opção: \n').lower()

            if opcao_venda == 'b':
                print("Compra finalizada!\nTotal da compra: R$", valorTotal)
                opçao_posVenda = input(print('''\nDeseja retornar ao menu inicial?
                1 - Sim
                2 - Não
                '''))

                if opçao_posVenda == 1:
                    continue
                
                if opçao_posVenda == 2:
                    print("Sessão finalizada.")
                    break

            if opcao_venda == 'c':
                continue

            while opcao_venda not in('a','b','c'):
                opcao_venda = input('''
                Opção inválida. 
                
                Menu de Vendas:
            
                a) Adicionar produtos ao carrinho;
                b) Finalizar a compra;
                c) Voltar ao menu anterior. 
                
                Escolha uma opção compatível: ''').lower()
                if opcao_cadastro == 'a':
                    pass
                if opcao_cadastro == 'b':
                    pass
                if opcao_cadastro == 'c':
                    continue
                
        case '3':
            print("""
            Menu de Relatório: 
            
            a) Obter extrato de produtos vendidos;
            b) Voltar ao menu anterior.

            """)
            opcao_extrato = input('Escolha uma opção: ').lower()
            if opcao_extrato == 'a':
                pass
            if opcao_extrato == 'b':
                continue
            while opcao_extrato not in('a','b'):
                opcao_extrato = input('''
                Opção inválida. 
                
                Menu de Vendas:
            
                a) Obter extrato de produtos vendidos;
                b) Voltar ao menu anterior.

                Escolha uma opção compatível: ''').lower()
                if opcao_extrato == 'a':
                    pass
                if opcao_extrato == 'b':
                    continue
                        
        case '4':
            print('Volte sempre!.')
            break
        
        case _:
            print('Opção Inválida.')