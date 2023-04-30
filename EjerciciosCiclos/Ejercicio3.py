#Determinar si un número es o no es perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio número es igual a este.
a=int(input('Escriba un numero: '))
b=2
sum=0
while b<=a:
    if a%b==0:
        sum+=a//b
    b+=1
if sum==a:
    print('El numero es perfecto')
else: print('El numero no es perfecto')
        