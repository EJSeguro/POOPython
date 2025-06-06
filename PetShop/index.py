from Classes.Animal import *
from Classes.Cachorro import *
from Classes.Gatos import *
from Classes.Aves import *
import os


animais = []
cadastrosTotais = 0

while True:
    os.system("cls")
    print("Escolha uma opção:")
    print("1. Cadastrar animal")
    print("2. Listar animals")
    print("3. Remover animal")
    print("4. Editar animal")
    print("5. Sair")
    opcao = int(input("Opção: "))
    try:
        if opcao == 1:
            while True:
                os.system("cls")
                opcaoAnimal = int(input("Qual animal você deseja criar?\n1. Cachorro\n2. Gato\n3. Ave\n4. Sair\nOpção: "))
                try:
                    opcaoAnimal = int(opcaoAnimal)
                    if opcaoAnimal == 1:
                        tipo = "Cachorro"
                    elif opcaoAnimal == 2:
                        tipo = "Gato"
                    elif opcaoAnimal == 3:
                        tipo = "Ave"
                except ValueError:
                    print("Opção inválida")
                if opcaoAnimal == 1 or opcaoAnimal == 2 or opcaoAnimal == 3:
                        while True:
                            os.system("cls")
                            try:
                                nome = input("Nome: ")
                            except ValueError:
                                print("Nome inválido")
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            try:
                                idade = int(input("Idade: "))
                            except ValueError:
                                print("Idade inválida")
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            try:
                                peso = float(input("Peso: "))
                            except ValueError:
                                print("Peso inválido")
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            try:
                                dono = input("Dono: ")
                            except ValueError:
                                print("Nome inválido") 
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            try:
                                raca = input("Raça: ")
                            except ValueError:
                                print("Nome inválido")
                                input("Voltando ao MENU... Pressione Enter")   
                                break
                            try:
                               pelagem = input("Plumagem: ") if opcaoAnimal == 3 else input("Pelagem: ")
                            except ValueError:
                                print("Cor inválido")
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            os.system("cls")
                            cadastrosTotais += 1
                            id = 1 if animais == [] else cadastrosTotais
                            ultimaModificacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                            if opcaoAnimal == 1:
                                animal = Cachorro(id,nome,idade,peso,dono,ultimaModificacao,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                                break
                            elif opcaoAnimal == 2:
                                animal = Gato(id,nome,idade,peso,dono,ultimaModificacao,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                                break
                            elif opcaoAnimal == 3:
                                animal = Ave(id,nome,idade,peso,dono,ultimaModificacao,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                                break
                            input("Voltando ao MENU... Pressione Enter")
                elif opcaoAnimal == 4:
                    input("Voltando ao MENU... Pressione Enter")
                    break
                else:
                    print("Opção inválida")
                    
        elif opcao == 2:
            os.system("cls")
            tipo = input("Qual tipo de animais você deseja listar? 1-Cachorros 2-Gatos 3-Aves 4-Todos: ")
            try:
                tipo = int(tipo)
                if tipo == 1:
                    tipo = "Cachorro"
                elif tipo == 2:
                    tipo = "Gato"
                elif tipo == 3:
                    tipo = "Ave"
                elif tipo == 4:
                    tipo = "Todos"
            except ValueError:
                print("Valor inválido")
                input("Voltando ao MENU... Pressione Enter")
            Animal.exibirAnimais(animais,tipo)
        elif opcao == 3:
                os.system("cls")
                try:
                    id = int(input("Qual animal você deseja remover? Digite o ID do animal: "))
                    animalEncontrado = None
                    for animal in animais:
                        if animal.id == id:
                            animalEncontrado = animal
                            break
                    if animalEncontrado == None:
                        print("Animal não encontrado")
                    else:
                        Animal.removerAnimal(animais,animalEncontrado)
                except ValueError:
                    print("Digite um ID válido")
                input("Voltando ao MENU... Pressione Enter")
        if opcao == 4:
            os.system("cls")
            try:
                animalEncontrado = None
                id = int(input("Qual animal você deseja editar? Digite o ID do animal: "))
                for animal in animais:
                    if animal.id == id:
                        animalEncontrado = animal
                        break
                if animalEncontrado == None:
                    print("Animal não encontrado")
                    input("Voltando ao MENU... Pressione Enter")
                else:
                    opcao = int(input("Qual informação você deseja alterar?\n1. Nome\n2. Idade\n3. Peso\n4. Dono\n5. Sair\nOpção: "))
                    try:
                        if opcao == 1 or opcao == 4:
                            modificacao = input("Digite o novo nome: ")
                        elif opcao == 2:
                            modificacao = int(input("Digite a nova idade: "))
                        elif opcao == 3:
                            modificacao = float(input("Digite o novo peso: "))
                        elif opcao == 5:
                            input("Voltando ao MENU... Pressione Enter")
                    except ValueError:
                        print("Valor inválido")
                    Animal.editarAnimal(animalEncontrado,opcao,modificacao)
                    input("Voltando ao MENU... Pressione Enter")
            except ValueError:
                print("Valor inválido")
                input("Voltando ao MENU... Pressione Enter")
        if opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida")        
    except ValueError:
        print("Opção inválida")