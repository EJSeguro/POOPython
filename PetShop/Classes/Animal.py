class Animal():

    def __init__(self,id,nome,idade,peso,dono):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dono = dono
        self.tipo = "Cachorro"

    def som():
        return "Barulho!"
    
    def exibirInfos(self):
        print(f"ID: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nDono: {self.dono}\nTipo: {self.tipo}")

    def removerAnimal(animais,id):
        for animal in animais:
            if animal.id == id:
                animais.remove(animal)
                print("------------------------------------")
                print(f"O animal {animal.nome} foi removido com sucesso!")
                sucesso = True
                break
        if not sucesso:
            print("Animal não encontrado")
        input("Voltando ao MENU... Pressione Enter")

    def exibirAnimais(animais):
        print("\n--- Lista de Animais Cadastrados ---")
        for animal in animais:
            animal.exibirInfos()
            print("------------------------------------")
        input("Pressione Enter para voltar...")