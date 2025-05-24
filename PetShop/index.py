from Classes.Cachorro import Cachorro
from Classes.Animal import Animal

cachorros = []
dog = Cachorro("Geraldo",2,5.6,"Roberto","Bulldog Frances","Preto")

cachorros.append(dog)

cachorros[0].exibirInfos()

print(cachorros[0].som())