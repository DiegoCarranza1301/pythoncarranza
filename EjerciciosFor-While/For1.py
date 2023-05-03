a=int(input('Ingrese la cantidad de numeros naturales: '))
while a<=0:
    print(f'El numero debe ser positivo')
    a=int(input('Ingrese la cantidad de numeros naturales: '))
suma=0
for b in range(1,a+1):
    elevar_cuadrado=a+a
    suma=suma+elevar_cuadrado
print(f'La suma de los numeros naturales es {suma}')