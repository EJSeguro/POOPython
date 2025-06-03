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
    print("4. Sair")
    opcao = int(input("Opção: "))
    try:
        if opcao == 1:
            while True:
                os.system("cls")
                opcao = int(input("Qual animal você deseja criar?\n1. Cachorro\n2. Gato\n3. Ave\n4. Sair\nOpção: "))
                try:
                    opcao = int(opcao)
                    if opcao == 1:
                        tipo = "Cachorro"
                    elif opcao == 2:
                        tipo = "Gato"
                    elif opcao == 3:
                        tipo = "Ave"
                except ValueError:
                    print("Opção inválida")
                if opcao == 1 or opcao == 2 or opcao == 3:
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
                               pelagem = input("Plumagem: ") if opcao == 3 else input("Pelagem: ")
                            except ValueError:
                                print("Cor inválido")
                                input("Voltando ao MENU... Pressione Enter")
                                break
                            os.system("cls")
                            cadastrosTotais += 1
                            id = 1 if animais == [] else cadastrosTotais
                            if opcao == 1:
                                animal = Cachorro(id,nome,idade,peso,dono,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                            elif opcao == 2:
                                animal = Gato(id,nome,idade,peso,dono,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                            elif opcao == 3:
                                animal = Ave(id,nome,idade,peso,dono,raca,pelagem)
                                animais.append(animal)
                                print(f"{animal.nome} foi cadastrado com sucesso!")
                            input("Voltando ao MENU... Pressione Enter")
                            break
                if opcao == 4:
                    break
                else:
                    print("Opção inválida")
        elif opcao == 2:
            Animal.exibirAnimais(animais)
        elif opcao == 3:
                os.system("cls")
                id = int(input("Qual animal você deseja remover? Digite o ID do animal: "))
                try:
                    Animal.removerAnimal(animais,id)
                except:
                    print("ID inválido")
                    while True:
                        os.system("cls")
                        opcao = input("Deseja tentar novamente? (S/N): ")
                        try:
                            if opcao == "N":
                                loop = False
                                break	
                            elif opcao == "S":
                                break
                        except:
                            print("Digite S ou N")
        elif opcao == 4:
            break
        else:
            print("Opção inválida")        
    except ValueError:
        print("Opção inválida")