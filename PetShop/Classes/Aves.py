from Classes.Animal import Animal
aves = []

class Ave(Animal):
    def __init__(self,id,nome,idade,peso,dono,ultimaModificacao,linhagem,plumagem):
        super().__init__(id,nome,idade,peso,dono,ultimaModificacao)
        self.linhagem = linhagem
        self.plumagem = plumagem
        self.tipo = "Ave"

    def exibirInfos(self):
        print(f"ID: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nDono: {self.dono}\nLinhagem: {self.linhagem}\nPlumagem: {self.plumagem}\nTipo: {self.tipo}\nÚltima Modificação: {self.ultimaModificacao}\nO animal faz: {self.som()}")

    def som(self):
        return "Piu Piu!"