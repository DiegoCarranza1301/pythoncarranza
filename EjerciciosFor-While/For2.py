a=int(input(f'cantidad de participantes: '))
print('Colombia-->Opcion1')
print('Argentina-->Opcion2')
cont=0
contador=0
for b in range (1,a+1):
    voto=int(input(f'Asistente numero {b}: '))
    while(voto<1 or voto>2):
        print(f'opcion no valida')
        voto=int(input(f'Asistente numero {b}: '))
    if voto==1:
        cont=cont+1
    if voto==2:
        contador+=1
print(f'Votos para Colombia son {cont}')
print(f'Votos para Argentina son {contador}')