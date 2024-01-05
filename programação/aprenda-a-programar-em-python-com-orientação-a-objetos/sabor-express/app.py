#Bibliotecas importadas
import os

#Declaração de variáveis
restaurantes = []

################### Definição de módulos ###################

#Finalização do programa
def finalizar_programa():
    os.system('cls')
    # os.system('clear') para Mac
    print("Encerrando o programa!")

#Caso o usuário insira uma opção inválida
def opcao_invalida():
    print("Opção inválida.\n")
    input("Digite uma tecla para voltar ao menu principal.")
    main()
        
#Exibição do nome do programa        
def exibir_nome_programa():
    print("""☆:.｡.o(≧▽≦)o.｡.:☆
Sabor Express     
☆:.｡.o(≧▽≦)o.｡.:☆\n""")

#Exibição das opções do programa
def exibir_opcoes():
    print("""    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar restaurante
    4. Sair\n""")

#Cadastro de restaurante
def cadastrar_novo_restaurante():
    os.system('cls')
    #os.system('clear') para Mac
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso.")
    input("Digite uma tecla para voltar ao menu principal.")
    main()

#Verifica a entrada do usuário.
#Caso o usuário digite o tipo errado ou número inexistente de opção,
#o programa executa a função opcao_invalida()
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print("Listando restaurantes")
        elif opcao_escolhida == 3:
            print("Ativando restaurante")
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    

#Programa principal
def main():
    os.system('cls')
    # os.system('clear') para Mac
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
