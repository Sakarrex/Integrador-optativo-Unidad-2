class IntegranteProyecto:
    __idProyecto = str
    __apellidoNombre = str
    __DNI = str
    __categoriaInvestigacion = str
    __rol = str

    def __init__(self, idProyecto = "Vacio", nombre = "Vacio", DNI = "Vacio", categoria= "Vacio", rol = "Vacio"):
        self.__idProyecto = str(idProyecto)
        self.__apellidoNombre = str(nombre)
        self.__DNI = str(DNI)
        self.__categoriaInvestigacion = str(categoria)
        self.__rol = str(rol)
    
    def getIdProyecto(self):
        return self.__idProyecto
    
    def getRol(self):
        return self.__rol
    
    def getNombre(self):
        return self.__apellidoNombre
    
    def getCategoria(self):
        return self.__categoriaInvestigacion