import random
lista=[random.sample(range(0,100),random.randint(1,10))]
def primult(lista):
    return [lista[0],lista[len(lista)-1]]
print(primult(lista))