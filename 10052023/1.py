# Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. Diseñe un menú con las siguientes operaciones.😁
# a. Imprimir arreglo original (El primero que se generó)😁
# b. Suma😁
# c. Promedio😁
# d. Mayor😁
# e. Menor😁
# f. Ordenar ascendente (No perder el arreglo original; el del punto a)😁
# g. Ordenar descendente (No perder el arreglo original; el del punto a)😁
# h. Moda
# i. Mediana
# j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está
import random
lista=[]
print()
print('Los numeros que le pediran es el numero inicial(hasta que numero se pueden generar de forma random), y el tamaño de la lista')
print()
a=int(input(f'Numero inicial: '))
b=int(input(f'Tamaño de la lista: '))
def llenarLista(a,b):
    lista=[random.randrange(a) for c in range (b)]
    return lista
def sumaLista(lista):
    suma=0
    for d in lista:
        suma+=d
    return suma
def promedioLista(lista):
    return sumaLista(lista)/b
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
def ascendenteLista(lista):
    for g in range (b-1):
        for h in range(g+1,b):
            if lista[g]>lista[h]:
                lista[g],lista[h]=lista[h],lista[g]
    return lista
def descenteLista(lista):
    for g in range (b-1):
        for h in range(g+1,b):
            if lista[g]<lista[h]:
                lista[g],lista[h]=lista[h],lista[g]
    return lista
def modaLista(lista):
    i=0
    for g in lista:
        cont=0
        for h in lista:
            if g==h:
                cont+=1
    if cont>i:
        i=cont
        moda=g
    return moda
l1=llenarLista(a,b)
print(l1)
print(f'la suma de la lista es {sumaLista(l1)}')
print(f'el promedio de la lista es {promedioLista(l1)}')
print(f'el numero mayor de la lista es {mayorLista(l1)}')
print(f'el numero menor de la lista es {menorLista(l1)}')
print(f'el orden ascendente de la lista es: \n{ascendenteLista(l1)}')
print(f'el orden descendente de la lista es: \n{descenteLista(l1)}')
print(f'{modaLista}')