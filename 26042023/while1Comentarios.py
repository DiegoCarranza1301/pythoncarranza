# num=1
# print(type(num))
# num="sena"
# print(type(num))

#se crea una variables con un numero
num=1
cont=0
sum=0
menor=1000000
mayor=0

#se crea un while con la variable num diciendo si no es igual a 0 entonces:
while num!=0:
    #se le asgina un int input a la varibel num con el texto 'ingrese numero'
    num=int(input('ingrese numero'))
    #se utiliza la variable cont con un resultado de este mismo mas 1
    cont=cont+1
    #se utiliza la variable sum con un resultado de sum+num
    sum=sum+num
    #se crea un if haciendo referencia a si (num) es mayor que (mayor)
    if num>mayor:
        #se le asigna a la variable mayor como resultado la variable num
        mayor=num
    #se crea un if haciendo referencia a si (num) es menor a (menor) y (num no es igual a 0)
    if num<menor and num!=0:
        #se le asigna a la variable(menor) como resultado la variable(num)
        menor=num

#se imprime en pantalla el texto 'fueron ingresados' junto a la varibale cont pero-1 en seguida con el texto 'numeros'
print(f'fueron ingresados {cont-1} numeros')
#se imprime el texto con la variable sum
print(f'La suma es {sum}')
#se imprime el texto 'el promedio es' junto a la variable (sum) divido con la variable (cont-1)
print(f'El promedio es {sum/(cont-1)}')
#se imprime en pantalla:
print(f'El mayor es {mayor}')
#se imprime en pantalla:
print(f'El menor es {menor}')