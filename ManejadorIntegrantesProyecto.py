from asyncio.windows_events import NULL
from csv import reader
import csv
import numpy as np
from ClaseIntegrantesProyecto import IntegranteProyecto

__cantidadDeIntegrantes = 11
__ArregloIntegrantesProyectos = np.empty(__cantidadDeIntegrantes,dtype=IntegranteProyecto)

archivo = open("integrantesProyecto.csv")
reader = csv.reader(archivo,delimiter=";")

banderaCabecera = True
i = 0
for files in reader:
    if banderaCabecera == True:
        banderaCabecera = False
    else:   
        NuevoIntegrante = IntegranteProyecto(files[0],files[1],files[2],files[3],files[4])
        __ArregloIntegrantesProyectos[i] = NuevoIntegrante
        i += 1
    
   

archivo.close

def getCantidadDeIntegrantesProyecto(idProyecto):
    valorADevolver = 0
    for i in range(len(__ArregloIntegrantesProyectos)):
        if __ArregloIntegrantesProyectos[i].getIdProyecto() == idProyecto:
            valorADevolver += 1
    return valorADevolver
    

def BuscarIntegrante(IdProyecto, rol):
    IntegranteADevolver = NULL
    i = 0
    bandera = False
    while i < len(__ArregloIntegrantesProyectos) and bandera == False:
        if __ArregloIntegrantesProyectos[i].getIdProyecto() == IdProyecto and __ArregloIntegrantesProyectos[i].getRol() == rol:
            bandera = True
            IntegranteADevolver = __ArregloIntegrantesProyectos[i]
        i+=1

    return IntegranteADevolver

getCantidadDeIntegrantesProyecto("21E239")
