print('- - - VOCÊ ENTROU NO SISTEMA DE ESTOQUE DA LOJA DE DISPOSTIVOS ELETRÔNICOS')

#This code is ugly and bad, I make it about 2 months ago and I am going to make many changes on it;
#Read the readme for more info
chave_de_acesso = input('Por favor, coloque a chave de acesso aqui:')
if chave_de_acesso == '3024':
    print('- - -VOCÊ ENTROU NO SISTEMA - - -')
    produtos = ['smartphone','notebook','tablet','smarttv','fonedeouvidobluetooth','headsetgamer','mousesemfio','tecladomecanico','monitor','impressora','scanner','webcam','caixadesombluetooth','smartwatch','consoledevideogame','controledevideogame','cameradigital','cameradeseguranca','roteadorwifi','modem','hdexterno','ssd','pendrive','powerbank','carregadorportatil','carregadorsemfio','drone','projetor','assistentevirtual','leitordeebook']
    print(produtos)

    print('O que você deseja escolher?')
    escolher_acao = input('A. Adicionar produto. B. Excluir produto. C. Área do Administrador. ').upper()
    if escolher_acao == 'A':
        add_produto_or_produtos = int(input('Você deseja adicionar quantos produtos?'))
        if add_produto_or_produtos > 1:
            novos_produtos = input('Você deseja adicionar quais produtos?(Por favor, separe por vírgula):')
            produtos.append(novos_produtos.lower())
            print(produtos)
        if add_produto_or_produtos == 1:
            novo_produto = input('Você deseja adicionar qual produto?:')
            produtos.append(novo_produto.lower())
            print(produtos)
    elif escolher_acao == 'B':
        del_produto_or_produtos = int(input('Você deseja deletar quantos produtos?'))
        if del_produto_or_produtos > 1:
         del_produtos = input('Quais produtos você deseja deletar?(Por favor, separe com vírgula):')
         for produto in del_produtos.lower().split(','):
             produto = produto.strip()
             if produto in produtos:
              produtos.remove(produto)
              print(produtos)
             else:
              print('Desculpe, seu produto não está na lista')
         
        if del_produto_or_produtos == 1:
            del_produto = input('Qual produto você deseja deletar?')
            produtos.remove(del_produto.lower())
            print(produtos)
    elif escolher_acao == 'C':
        print('você entrou na área do administrador, por favor, coloque sua chave de acesso')
        login = input('LOGIN:')
        if login == '8055':
            print('Acesso à área do administrador, por favor, escolha suas opções:')
            escolha_login = input('A. Calcular total de produtos. B. Calcular média mensal. C. Consultar/Modificar lista de funcionários. D. Voltar: ').upper()
            if escolha_login == 'A':
                total_de_produtos = len(produtos)
                print(f'O total de produtos no estoque é de: {total_de_produtos} produtos.')
            if escolha_login == 'B':
                primeiro_mes = float(input('Qual é o valor do primeiro mês? '))
                segundo_mes = float(input('Qual é o valor do segundo mês? '))
                terceiro_mes = float(input('Qual é o valor do terceiro mês? '))
                quarto_mes = float(input('Qual é o valor do quarto mês? '))
                quinto_mes = float(input('Qual é o valor do quinto mês? '))
                sexto_mes = float(input('Qual é o valor do sexto mês? '))
                setimo_mes = float(input('Qual é o valor do sétimo mês? '))
                oitavo_mes = float(input('Qual é o valor do oitavo mês? '))
                nono_mes = float(input('Qual é o valor do nono mês? '))
                decimo_mes = float(input('Qual é o valor do décimo mês? '))
                decimo_primeiro_mes = float(input('Qual é o valor do décimo primeiro mês? '))
                decimo_segundo_mes = float(input('Qual é o valor do décimo segundo mês? '))
                valor_total_ano = (primeiro_mes + segundo_mes + terceiro_mes + quarto_mes + quinto_mes +
                   sexto_mes + setimo_mes + oitavo_mes + nono_mes + decimo_mes +
                   decimo_primeiro_mes + decimo_segundo_mes) 
                media_mensal = (valor_total_ano / 12) 
                print("O valor total do ano é:", valor_total_ano)
                print('A média mensal é:', media_mensal)


        
            if escolha_login == 'C':
                funcionarios = ["alice", "bruno", "carla", "diego", "eduardo", "fernanda", "gabriel", "helena", "igor", "juliana"]
                print(funcionarios)
                demitir_ou_contratar = input('Você deseja: A. Contratar funcionário. B. Demitir funcionário. C. Voltar').upper()
                if demitir_ou_contratar == 'A':
                    contratar_funcionario = input('Qual funcionário você gostaria de contratar?(Por favor, coloque somente o primeiro nome):')
                    funcionarios.append(contratar_funcionario.lower())
                elif demitir_ou_contratar == 'B':
                    demitir_funcionario = input('Qual funcionário você gostaria  de demitir?(Por favor, coloque somente o primeiro nome):')
                    if demitir_funcionario in funcionarios:
                     funcionarios.remove(demitir_funcionario.lower())
                    else:
                        print('Desculpe, o funcionário não está na lista')
                elif demitir_ou_contratar == 'C':
                    print('Voltando ao menu anterior...')






else:
         print('Chave de acesso bloqueada!')