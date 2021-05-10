class Alumno:
    __nombre = None
    __anio = None
    __division = None
    __inasistencias = None
    maxInasistencias = 13
    cantTotaldeClases = 120

    def __init__(self, nombre, anio, division, inasistencias):
        self.__nombre = nombre
        self.__anio = anio
        self.__division = division
        self.__inasistencias = inasistencias
    
    def getNombre (self):
        return self.__nombre
    
    def getAnio (self):
        return self.__anio
    
    def getDivision (self):
        return self.__division
    
    def getInasistencias (self):
        return self.__inasistencias
        
    @classmethod
    def getMaximoInasistencias (self):
        return self.maxInasistencias
    
    @classmethod
    def getCantTotaldeClases (self):
        return self.cantTotaldeClases
    
    def getPorcentaje(self):
        return (int(self.__inasistencias)*100)/Alumno.cantTotaldeClases

    @classmethod
    def modificarInasistencias(self,nuevo):
        Alumno.maxInasistencias = nuevo
