class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__curso=[]
    def getNombre(self):
        return self.__nombre
    def getDoc(self):
        return self.__documento
    def setNom(self,nombre):
        self.__nombre=nombre
    def setDoc(self,documento):
        self.__documento=documento
    def getCurso(self):
        return self.__curso
    def setCurso(self,curso):
        self.__curso=curso
    # def buscarCurso(self):
p=Persona('diego', 1024501189)
print(p.getNombre())
print(p.getDoc())
p.setCurso(['matematicas', 'algebra', 'fisica', 'ed. fisica', 'español'])
print(p.getCurso())