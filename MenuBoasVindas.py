while True:
    print(
    """
╠══============================ BOAS-VINDAS =================================══╣
  ____    _____     _____              _   _   _____    _____    ____     _____ 
 / __ \  |  __ \   / ____|     /\     | \ | | |_   _|  / ____|  / __ \   / ____|
| |  | | | |__) | | |  __     /  \    |  \| |   | |   | |      | |  | | | (___  
| |  | | |  _  /  | | |_ |   / /\ \   | . ` |   | |   | |      | |  | |  \___ \ 
| |__| | | | \ \  | |__| |  / ____ \  | |\  |  _| |_  | |____  | |__| |  ____) |
 \____/  |_|  \_\  \_____| /_/    \_\ |_| \_| |_____|  \_____|  \____/  |_____/ 

╠══========================= MENU DE NAVEGAÇÃO ==============================══╣

                                1-CADASTRO 
                                2-VENDAS 
                                3-RELATÓRIO 
                                4-SAIR 
                              """)
    opcao = input("""
                        iNFORME A OPÇÃO DESEJADA:""")
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
            if opcao_cadastro == 'a':
                pass
            if opcao_cadastro == 'b':
                pass
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
                if opcao_cadastro == 'a':
                        pass
                if opcao_cadastro == 'b':
                    pass
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
            if opcao_venda == 'a':
                pass
            if opcao_venda == 'b':
                pass
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