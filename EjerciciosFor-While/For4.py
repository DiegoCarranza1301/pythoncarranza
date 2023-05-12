num=int(input(f'Ingrese un numero: '))
contador=0
for b in range(1,num+1):
    if num%b==0:
        contador=contador+1
if contador>2:
    print(f'el numero {num} no es primo')
else:
    print(f'el numero {num} es primo')