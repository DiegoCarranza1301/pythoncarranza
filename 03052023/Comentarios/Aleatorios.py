import random #Se importa el modulo random
num=int(random.random()*10)#se crea una variable de tipo entero donde se genere con el random.random un numero del 0 al 10, en este caso solo va ir hasta 9
print(num)#se imprime en pantalla la variable {num}
num1=random.randint(0,100)#se crea una variable {num1} con un random.randint, donde es otra forma de imprimir los numero pero estos deben ser obligatoriamente de tipo entero, esta va de 0 a 100 
print(num1)#se imprime en pantalla la variable
num2=random.randrange(10)#se crea una variable {num2} con un random.randrange donde esta ya va de un rango de 0 a 10 ya que solo hay un numero
print(num2)#se imprime en pantalla la variable