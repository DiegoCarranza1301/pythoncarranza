class Empleado:
    def __init__(self,nombre,cargo):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=int()
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
e1=Empleado('Diego', 'Inspector')
print(e1.aggNom())
print(e1.aggCarg())
print(e1.sal)