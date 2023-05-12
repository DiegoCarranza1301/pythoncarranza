#se crea unas variables (x) y (y) con unos numeros como resultados
x,y=3,5
#se crea un cont con el resultado 1
cont=1
#se crea un while con un not que tengfa la varaible x con % y  que sea igual a 0 y un or que de como (y) con % en (x) con un igual 0
while not(x%y==0 or y%x==0):
    #se imprime un texto junto a la variable (cont)
    print(f'intento numero {cont}')
    #se le asigan al (x) y al (y) un int input
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    #se crea un cont con un mas o igual a 0
    cont+=1

#se imprime el resultado de(x) y (y) son factor
print(f'{x} y {y} son factor')