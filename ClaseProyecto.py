class Proyecto:
    __idProyecto = str
    __titulo = str
    __palabrasClave = str
    __puntaje = int

    def __init__(self, idProyecto = "Vacio", titulo = "Vacio", palabrasClave = "Vacio"):
        self.__idProyecto = str(idProyecto)
        self.__titulo = str(titulo)
        self.__palabrasClave = str(palabrasClave)
        self.__puntaje = 0
    
    def getIdProyecto(self):
        return self.__idProyecto
    
    def getTitutlo(self):
        return self.__titulo
    
    def getPalabrasClave(self):
        return self.__palabrasClave
    
    def getPuntaje(self):
        return self.__puntaje
    
    def ModificarPuntaje(self,puntaje):
        self.__puntaje = int(puntaje)
    
    def __gt__ (self, otro):
        if type(otro) == Proyecto:
            return  otro.getPuntaje() > self.__puntaje