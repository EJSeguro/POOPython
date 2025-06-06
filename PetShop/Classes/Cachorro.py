from Classes.Animal import Animal
cachorros = []

class Cachorro(Animal):
    def __init__(self,id,nome,idade,peso,dono,ultimaModificacao,raca,pelagem):
        super().__init__(id,nome,idade,peso,dono,ultimaModificacao)
        self.raca = raca
        self.pelagem = pelagem
        self.tipo = "Cachorro"

    def som(self):
        return "Au Au!"

