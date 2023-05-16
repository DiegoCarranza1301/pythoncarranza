# Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:\n😁
# a. Cuál de los dos tiene la suma más alta😁
# b. Cuál de los dos tiene el número mayor😁
# c. Cuál de los dos tiene el número menor😁
# d. Cuál es el promedio conjunto (uniendo los dos arreglos)😁
# e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto😁
# f. Cuál de los dos tiene mayor cantidad de pares
# g. Cuál de los dos tiene mayor cantidad de impares
import random
lista=[]
a=100
b=10
def llenarLista(a,b):
    lista=[random.randrange(a) for c in range (b)]
    return lista
def sumaLista(lista):
    suma=0
    for d in lista:
        suma+=d
    return suma
l1=llenarLista(a,b)
l2=llenarLista(a,b)
print(f'lista1: \n{l1}')
print(f'La suma de la lista1 es igual a {sumaLista(l1)}')
print(f'lista2: \n{l2}')
print(f'La suma de la lista2 es igual a {sumaLista(l2)}')
print()
if sumaLista(l1)>sumaLista(l2): print(f'la suma de la lista1 es la mayor')
else: print(f'la suma de la lista2 es la mayor')
def mayorLista(lista):
    mayor=0
    for e in lista:
        if e>mayor:
            mayor=e
    return mayor
def menorLista(lista):
    menor=1000000
    for f in lista:
        if f<menor:
            menor=f
    return menor
if mayorLista(l1)>mayorLista(l2):print(f'el numero mayor de las dos listas es {mayorLista(l1)} de la lista1')
else:print(f'el numero mayor de las dos listas es {mayorLista(l2)} de la lista2')
if menorLista(l1)<menorLista(l2): print(f'el numero menor de las dos listas es {menorLista(l1)} de la lista1')
else:print(f'el numero menor de las dos listas es {menorLista(l2)} de la lista2')
def promedioLista(lista):
    return sumaLista(lista)/b
print()
conjuntoListas=(l1+l2)
print(conjuntoListas)
sumaLista(conjuntoListas)
print(promedioLista(conjuntoListas))
if promedioLista(l1)>promedioLista(conjuntoListas):print(f'el promedio de la lista1: {promedioLista(l1)} es mayor que el promedio en conjunto: {promedioLista(conjuntoListas)}')
if promedioLista(l2)>promedioLista(conjuntoListas):print(f'el promedio de la lista2: {promedioLista(l2)} es mayor que el promedio en conjunto: {promedioLista(conjuntoListas)}')
else:print(f'el promedio del conjunto de las listas: {promedioLista(conjuntoListas)} es mayor que el promedio de las lista1 y lista2')  