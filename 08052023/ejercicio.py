import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
for e in range(tam-1):
    for f in range(e+1,tam):
        if lista[e]>lista[f]:
            lista[e],lista[f]=lista[f],lista[e]
print(lista)