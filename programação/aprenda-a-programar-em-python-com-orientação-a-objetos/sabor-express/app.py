print("""☆:.｡.o(≧▽≦)o.｡.:☆
Sabor Express     
☆:.｡.o(≧▽≦)o.｡.:☆
      
1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar restaurante
4. Sair\n""")

opcao_escolhida = input("Escolha uma opção: ")

if opcao_escolhida == 1:
    print("Cadastrando restaurante")
elif opcao_escolhida == 2:
    print("Listando restaurantes")
elif opcao_escolhida == 3:
    print("Ativando restaurante")
else:
    print("Encerrando o programa")