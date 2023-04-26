#Se crea dos variables y asignamos su valor correspondiente en la misma linea separados por una coma
num1,num2=100,50
#Con la función print() se escribe un mensaje de suma, resta, multiplicación, division y residuo para cada caso
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
#Se cra una varible una variable de tipo input entera con el denunciado de "que operación?"
op=int(input('que operacion?'))
#Se utiliza la variable match que nos servirá para condicionar la variable op pero de una manera más simplificada
match op:
    case 1:#En cada caso imprimiremos la operacion que queremos hacer con las dos variables
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)
    #se mostrara el resultado de cada operacion segun corresponda