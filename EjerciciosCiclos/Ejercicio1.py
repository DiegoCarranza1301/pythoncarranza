#Determinar los divisores de un número introducido por teclado
a=int(input('Escriba un numero: '))
contador=0
print(f'Los divisores de {a} son: ')
for b in range(1,a+1):
    if a%b==0:
        print(f'{b}')
        contador+=1