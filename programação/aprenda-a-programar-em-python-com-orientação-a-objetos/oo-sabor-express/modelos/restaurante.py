class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante_praca = Restaurante('Praça', 'Goumert')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurante()

#dir() - mostra todas as classes do objeto
#print(dir(restaurante_praca))

#vars() - mostra um dicionário com os atributos da classe do objeto
#print(vars(restaurante_praca))

#mostra o valor do atributo
#print(restaurante_praca.ativo)
