import random
suma=0
cont=0
mayor=0
menor=1000
lista=[]
tam=random.randint(10,20)

for a in range(tam):
    b=random.randrange(100)
    lista.append(b)
print(lista)
for c in lista:
    suma+=c
    cont+=1
print(f'las suma es {suma}')
for d in lista:
     if d>mayor:
         mayor=d
     if d<menor:
         menor=d
print(f'El numero mayor es {mayor}')
print(f'el numero menor es {menor}')