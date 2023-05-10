import random

lista=[]
tam=random.randint(15,20)

print (tam)
for a in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista)
num=int(input('ingrese un numero: '))
while num not in lista:
    num=int(input('El numero no se encuentra en la lista, ingrese otro: '))
for b in lista:
    contador=0
    for c in lista:
        if num==c:
            contador+=1
print(f'El numero se encuentra {contador} veces')

for d in range(len(lista)):
    if num==lista[d]:
        print(f'{lista[d]} esta en la posición {d}')