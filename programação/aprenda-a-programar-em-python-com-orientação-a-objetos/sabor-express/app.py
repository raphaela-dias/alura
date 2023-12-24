#Bibliotecas importadas
import os

#Definição de módulos
def finalizar_programa():
    os.system('cls')
    # os.system('clear') para Mac
    print("Encerrando o programa!")

def exibir_nome_programa():
    print("""☆:.｡.o(≧▽≦)o.｡.:☆
Sabor Express     
☆:.｡.o(≧▽≦)o.｡.:☆\n""")

def exibir_opcoes():
    print("""    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar restaurante
    4. Sair\n""")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        print("Cadastrando restaurante")
    elif opcao_escolhida == 2:
        print("Listando restaurantes")
    elif opcao_escolhida == 3:
        print("Ativando restaurante")
    else:
        finalizar_programa()
    

#Programa principal
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
