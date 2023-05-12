import random#se importa el modulo random
lista=[]#se hace una variable lista con un valor vacio
cuadrado=[]#se crea otra variable cuadrado con un valor vacio
tam=random.randint(5,10)#se crea una variable tam con el random.randint para que se hagan enteros entre 5 y 10
print(tam)#se imprime la variable tam
for i in range(tam):#se crea un for con una variable {i} con un rango de valor{tam}
    num=random.randrange(100)#se crea una variable num con el metodo random.randrange con un valor de 100
    lista.append(num)#la lista.append es para agregar a esta misma la variable {num}
print(lista)#se imprime la variable{lista}

for i in range(len(lista)):#se crea otro for con la variable con un rango que de la cuenta de los datos de la variable lista
    cuadrado.append(lista[i]**2)#se le agrega el metodo .append a la lista cuadrado con la variable lista por dentro donde {i}**2 hace referencia a que esta elevado a la 2
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)
print(sum(lista))
#se imprimen la lista cuadrado, y la lista{lista} pero esta ultima con la funcion sum