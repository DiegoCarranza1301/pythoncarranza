import random
lista1=[]
inicio1=int(input('ingrese un rango inicial: '))
final1=int(input('ingrese un rango final: '))
suma1=0
suma2=0
contador=0
par=0
impar=0
tam=random.randint(inicio1,final1)
promedioconj=0
for b in range(tam):
    num=random.randrange(10)
    lista1.append(num)
print(f'Lista1 generada de forma random: \n{lista1}')
for c in lista1: 
    suma1+=c
    contador+=1
promedio1=suma1/tam
lista2=[]
inicio2=int(input('ingrese un rango inicial: '))
final2=int(input('ingrese un rango final: '))
tam=random.randint(inicio2,final2)
for b in range(tam):
    num=random.randrange(10)
    lista2.append(num)
print(f'Lista2 generada de forma random: \n{lista2}')
for c in lista2: 
    suma2+=c
    contador+=1
print(f'La suma de los numeros de la lista1 es {suma1}')
print(f'La suma de los numeros de la lista2 es {suma2}')
promedio2=suma2/tam
if suma1>suma2:
    print(f'la suma de la lista1 es mayor que la de la lista2')
else: print(f'la suma de la lista2 es mayor que la de la lista1')
Lista=[lista1+lista2]
print(f'la lista en conjunto es: \n {Lista}')
promedioconj=(promedio1+promedio2)/2
print(f'el promedio en conjunto es {promedioconj}')
print(f'el promedio de la lista1 de numeros es {promedio1}')
if promedio1>promedioconj:
    print(f'el promedio de la lista1 es mayor que el el promedio en conjunto')
print(f'el promedio de la lista2 de numeros es {promedio2}')
if promedio2>promedioconj:
    print(f'el promedio de la lista2 es mayor que el el promedio en conjunto')
if promedioconj>promedio1 or promedioconj>promedio2:
    print(f'el promedio en conjunto sigue siento mayor')
for d in lista1:
    if par!=0:
        print(d)