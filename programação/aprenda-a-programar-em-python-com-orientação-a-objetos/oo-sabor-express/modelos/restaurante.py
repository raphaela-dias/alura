class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurante():
        print(f"{'Nome do restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'} ")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return '✓' if self._ativo else '✗'

restaurante_praca = Restaurante('Praça', 'Goumert')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurante()

#dir() - mostra todas as classes do objeto
#print(dir(restaurante_praca))

#vars() - mostra um dicionário com os atributos da classe do objeto
#print(vars(restaurante_praca))

#mostra o valor do atributo
#print(restaurante_praca.ativo)
