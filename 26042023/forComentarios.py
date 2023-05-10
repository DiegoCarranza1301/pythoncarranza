#se crea un for con una variable con un rango de 11
for i in range(11):
    #se crea un if en referencia a si (i) tiene de residuo 3 con un igual igual 
    if i%3==0:
        #se imprime en pantalla el reesultado de (i) con el texto 'es multiplo de 3'
        print(f'{i} es multiplo de 3')
    #se crea un else para cerrar el if con un print que arroje lo que da el resultado (i)
    else:
        print(i)


#se crea un for con una variable (j) donde se hace un rango de 1 a 11 (es decir va hasta 10)
for j in range(1,11):
    print(j)
    #se imprime en pantalla el resultado de j

#se crea un for con una variable k donde el rango va de 0 a 10 pero este va aumentando de 2 en 2 (0,2,4...)
for k in range(0,11,2):
    print(k)

#se crea un for con una variable i en donde el rango va de 20 a 0 pero en este caso este va dismninuyendo de 2 en 2 (20, 18, 16...)
for i in range(20,0,-2):
    print(i)