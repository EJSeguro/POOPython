from Classes.Animal import Animal
gatos = []

class Gato(Animal):
    def __init__(self,id,nome,idade,peso,dono,ultimaModificacao,raca,pelagem):
        super().__init__(id,nome,idade,peso,dono,ultimaModificacao)
        self.raca = raca
        self.pelagem = pelagem
        self.tipo = "Gato"

    def som(self):
        return "Miau!"

