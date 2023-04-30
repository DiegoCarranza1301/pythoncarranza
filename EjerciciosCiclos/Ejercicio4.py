#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?
for a in range(1,1001):
    b=2
    suma=0
    while b<=a:
        if a%b==0:
            suma+=a//b
        b+=1
    if suma==a:
        print(f'{a} el numero es perfecto')
    else: print (a)