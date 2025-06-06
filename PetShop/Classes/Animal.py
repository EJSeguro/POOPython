import datetime

class Animal():

    def __init__(self,id,nome,idade,peso,dono, ultimaModificacao):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dono = dono
        self.tipo = ""
        self.ultimaModificacao = ultimaModificacao

    def som():
        return "Barulho!"
    
    def exibirInfos(self):
        print(f"ID: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nDono: {self.dono}\nTipo: {self.tipo}\nÚltima Modificação: {self.ultimaModificacao}\nO animal faz: {self.som()}")

    def removerAnimal(animais,animal):
        animais.remove(animal)
        print("------------------------------------")
        print(f"O animal {animal.nome} foi removido com sucesso!")


    def exibirAnimais(animais,tipo):
        print("\n--- Lista de Animais Cadastrados ---")
        if tipo == "Todos":
            for animal in animais:
                animal.exibirInfos()
                print("------------------------------------")
        else:
            for animal in animais:
                if animal.tipo == tipo:
                    animal.exibirInfos()
                    print("------------------------------------")
        input("Pressione Enter para voltar...")

    def editarAnimal(animal,opcao,modificacao):
        if opcao == 1:
            animal.nome = modificacao
            print(f"Nome alterado com sucesso!")
        elif opcao == 2:
            animal.idade = modificacao
            print(f"Idade alterada com sucesso!")
        elif opcao == 3:
            animal.peso = modificacao
            print(f"Peso alterado com sucesso!")
        elif opcao == 4:
            animal.dono = modificacao
            print(f"Dono alterado com sucesso!")
        elif opcao == 5:
            if animal.tipo != "Ave":
                animal.pelagem = modificacao
                print(f"Pelagem alterada com sucesso!")
            else:
                animal.plumagem = modificacao
                print(f"Plumagem alterada com sucesso!")
        animal.ultimaModificacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

