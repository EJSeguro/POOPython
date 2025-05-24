from Classes.Animal import Animal

class Cachorro(Animal):
    def __init__(self,nome,idade,peso,dono,raca,pelagem):
        super().__init__(nome,idade,peso,dono)
        self.raca = raca
        self.pelagem = pelagem
    
    def exibirInfos(self):
        print(f"{self.nome}, {self.idade}, {self.peso}, {self.dono}, {self.raca}, {self.pelagem}")

    def som(self):
        return "latido!"
