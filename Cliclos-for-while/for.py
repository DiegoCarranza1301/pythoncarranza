#Solicite al usuario inicio, fin y cantidad  incrementar o decrementar segun el caso. Imprima la serie
n=int(input("mostrar lo multiplos de: "))
for a in range(int (input('ingrese un numero inicial: ')), int (input('ingrese el numero final: ')), int (input('ingrese el incrementar(+) o decrementar(-): '))):
    if a%n==0:
        print(f'{a} es multiplo de {n}')
    else: print(a)