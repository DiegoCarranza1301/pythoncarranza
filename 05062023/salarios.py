class Empleado:
    salarios=[]
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
    def Nom(self, nombre):
        self.__nombre=nombre
    def Carg(self,cargo):
        self.__cargo=cargo
    def Sal(self,salario):
        self.__salario=salario
    def aggNom(self):
        return self.__nombre
    def aggCarg(self):
        return self.__cargo
    def aggSal(self):
        return self.__salario  
    def calSalxHora(self):
        return round(self.__salario/30/8)
    def IPC(self):
        return round (self.__salario/30/8*(12.8/100))
    def IPCsalario(self):
        return round (self.__salario+(self.__salario/30/8*(12.8/100)))
    #def minSalario(self):
    #    if self.__salario<=1300606:
    #        return round (self.__salario+(self.__salario/30/8*(12.8/100)))
e1=Empleado('Diego', 'Inspector', 2000000)
print('NOMBRE: ')
print(e1.aggNom())
print()
print('CARGO: ')
print(e1.aggCarg())
print()
print('SALARIO: ')
print(e1.aggSal())
print()
print('SALARIO*HORA: ')
print(e1.calSalxHora())
print()
print('IPC SALARIO: ')
print(e1.IPC())
print()
print('SALARIO + IPC: ')
print(e1.IPCsalario())
print()
print()
print()
e2=Empleado('Nestor', 'empleado', 1700000)
print('NOMBRE: ')
print(e2.aggNom())
print()
print('CARGO: ')
print(e2.aggCarg())
print()
print('SALARIO: ')
print(e2.aggSal())
print()
print('SALARIO*HORA: ')
print(e2.calSalxHora())
print()
print('IPC SALARIO: ')
print(e2.IPC())
print()
print('SALARIO + IPC: ')
print(e2.IPCsalario())
print()