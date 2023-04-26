#imprimir una serie de numeros n, cada vez que encuentre un multiplo de 7 debe indicarlo

numero=int (input('ingrese un numero'))
n=1
while n<numero:
    n+=1 
    if n%7==0:
        print(f'{n} es multiplo de 7')
    else:
        print(n)
        