import os

#Estrutura de um dicionário + lista [{}], onde é passado a Chave + Valor.

restaurantes = [{'nome': 'Mahai', 'categoria':'Japonesa', 'ativo':False}
                ,{'nome': 'BK', 'categoria':'Hamburguer', 'ativo':True},
                 {'nome': 'Oca', 'categoria':'Geral', 'ativo':False}]

def alterar_estado():
    exibir_subtitulos('ALTERANDO ESTADO DO RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
            if not restaurante_encontrado: #Foi colocado o 'not' pq para entrar dentro da condicional tem que ser verdadeiro.
                print('Restaurante não encontrado.')
    voltar_menu()

def opcao_invalida():
    print('Opção inválida!')
    voltar_menu()

def exibir_nome():
    print('Sabor Express\n')

def listar_restaurantes():
    exibir_subtitulos('RESTAURANTES LISTADOS:')
    
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado' #Caso verdadeiro exibir o primeiro valor, caso contrário, exibir o segundo.
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu()

def cadastrar_restaurante():
    exibir_subtitulos('CADASTRO DE NOVOS RESTAURANTES')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}:')
    
    #criando dicionário do restaurante que está sendo cadastrado.
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}

    restaurantes.append(dados_restaurante)

    #restaurantes.append(nome_restaurante) - ".append" para colocar o nome inserido dentro da lista.
    print(f'O restaurante {nome_restaurante} foi cadastrado!\n')
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app.')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulos(texto):
   os.system('cls') 
   linha = '*' * (len(texto))
   print(linha)
   print(texto)
   print(linha)
   print()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()