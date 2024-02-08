#Bibliotecas importadas
import os

#Declaração de variáveis
restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Pizza', 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana', 'ativo' : False}]

################### Definição de módulos ###################

#Exibição do nome do programa        
def exibir_nome_programa():
    print("""☆:.｡.o(≧▽≦)o.｡.:☆
Sabor Express     
☆:.｡.o(≧▽≦)o.｡.:☆\n""")


#Exibição do subtítulo
def exibir_subtitulo(texto):
    os.system('cls')
    #os.system('clear') para Mac
    print(texto)
    print()


#Exibição das opções do programa
def exibir_opcoes():
    print("""    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar restaurante
    4. Sair\n""")


#Verifica a entrada do usuário.
#Caso o usuário digite o tipo errado ou número inexistente de opção,
#o programa executa a função opcao_invalida()
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativando restaurante")
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


#Caso o usuário insira uma opção inválida
def opcao_invalida():
    print("Opção inválida.\n")
    voltar_ao_menu()


#Opção 1: Cadastro de restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}.")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria' : categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n")

    voltar_ao_menu()


#Opção 2: Listagem de restaurantes cadastrados
def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        
        print(f" - {nome} | {categoria} | {ativo}")
    
    voltar_ao_menu()


#Opção 4: Finalização do programa
def finalizar_programa():
    exibir_subtitulo("Encerrando o programa!")
        

#Volta ao menu principal
def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal. ")
    main()


#Programa principal
def main():
    os.system('cls')
    # os.system('clear') para Mac
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
