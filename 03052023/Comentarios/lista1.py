#[], {}, (), {()}
x=100#se crea una variable con valor 100
print(type(x))#se pone un print donde imprima el tipo de dato que es x
x='Soacha'#se le asgina otro valor a {x},
print(type(x))#Se imprime de que tipo es la varibale {x}
lista=['python',100,[1,2,3,[]],'a']#se crea una variable lista donde alamacena varios datos de diferente tipo
print(type(lista))#se imprime el tipo de la variable lista
print(len(lista))#se imprime el numero de datos que hay en la lista
print(lista[0])#se imprime el dato que este en la posicion 0
print(lista[1])#se imprime el dato que este en la posicion 1
print(lista[3])#se imprime el dato que este en la posicion 3
print(lista[-4])#se imprime el 4 dato, pero de reversa ya que tiene un -, en este si se comienza desde -1 ya que -0 no existe o es igual a 0.

del lista[-2]#este es para eliminar un dato especifico- en este caso seria eliminar el dato -2, osea el que va antes de {a}
print(lista)#se imprime la lista

"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""