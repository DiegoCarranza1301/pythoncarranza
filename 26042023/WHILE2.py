while True:
    NUMERO1=int (input('ingrese un numero: '))
    NUMERO2=int (input('ingrese otro numero: '))

    if NUMERO1 % NUMERO2== 0:
        print ('el ', NUMERO1, 'es factor de', NUMERO2)
        break
    elif NUMERO2%NUMERO1==0:
        print ('el ', NUMERO2, 'es factor de ', NUMERO1)
