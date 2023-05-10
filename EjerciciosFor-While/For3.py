a=int(input(f'Ingrese la cantidad de notas: '))
lista=[]
producto=1
for b in range(a):
    nota=int(input(f'Ingrese la nota: '))
    lista.insert(b, nota)
    producto=producto*lista[b]
print(lista)
print(f'El producto de los valores ingresados es: {producto}')