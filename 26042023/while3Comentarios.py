#se crea una variable n con un in input donde se pida ingresar un numero
n=int(input('ingrese numero'))
#se crea una variable i con resultado de 1
i=1
#se crea un while haciendo referencia a si (i) es menor que (n)
while i<n:
    #se crea un if con la variable i y %7 con un igual igual
    if i%7==0:
        #se imprime en pantalla la variable i con el texto 'es multiplo de 7'
        print(f'{i} es multiplo de 7')
    #se cierra el else con un print, imprimiendo asi la varaible(i)
    else:
        print(i)
    #por ultimo se pone i+= a 1
    i+=1