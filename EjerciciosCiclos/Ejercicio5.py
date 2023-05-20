# ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?
for a in range (1,1001):
    if a%2==0:
        print(f'{a}')
    else: print(f'{a} es numero primo')