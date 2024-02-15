class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Goumert')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

#dir() - mostra todas as classes do objeto
#print(dir(restaurante_praca))

#vars() - mostra um dicionário com os atributos da classe do objeto
#print(vars(restaurante_praca))

#mostra o valor do atributo
#print(restaurante_praca.ativo)

#print(restaurante_praca)
#print(restaurante_pizza)

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
