from Classes.Animal import Animal
gatos = []

class Gato(Animal):
    def __init__(self,id,nome,idade,peso,dono,raca,pelagem):
        super().__init__(id,nome,idade,peso,dono)
        self.raca = raca
        self.pelagem = pelagem
        self.tipo = "Gato"
    def exibirInfos(self):
        print(f"ID: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nDono: {self.dono}\nRaça: {self.raca}\nPelagem: {self.pelagem}\nTipo: {self.tipo}")

    def som(self):
        return "Miado!"

