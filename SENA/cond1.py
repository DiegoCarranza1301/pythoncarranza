#se crea una variable x de valor int con un input
x=int(input('ingrese numero'))
#se crea una variable y de valor int con un input
y=int(input('ingrese numero'))
#se crea una variable z de valor int con un input
z=int(input('ingrese numero'))
#indentación

#se crea un if en referencia a si x es menor que y entonces
if x>y:
    #se crea otro if con referencia a si x es menor que z entonces
    if x>z:
        #se crea un print para que muestre en pantalla el mensaje de 'el mayor es' y la variable x
        print(f'el mayor es {x}')
    #se crea un else con referencia a que si if da negativo o falso entonces
    else:
        #se muestra en pantalla el mensaje de 'el mayor es ' junto a la variable z
        print(f'el mayor es {z}')
#se crea otro else cerrando asi el primer if   
else:
    #se crea un if con referencia a que pasaria si y es mayor que z
    if y>z:
        #se muestra en pantalla el mensaje de 'el valor es' junto a la variable y
        print(f'el mayor es {y}')
    #se crea un else cerrando asi que pasaria si es falso if
    else:
        #por ultimo se muestra el mensaje de 'el mayor es' junto a la variable z
        print(f'el mayor es {z}')