#¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?
for a in range(0,1001):
    if a%2==0:
        print(f'{a} es numero es primo')
    else: print(a)