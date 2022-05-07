from asyncio.windows_events import NULL
from csv import reader
import csv

from numpy import sort
from ClaseProyecto import Proyecto
import ManejadorIntegrantesProyecto

listaProyectos = []

archivo = open("proyectos.csv")
reader = csv.reader(archivo, delimiter = ";")


banderaCabecera = True
for file in reader:
    if banderaCabecera == True:
        banderaCabecera = False
    else:
        listaProyectos.append(Proyecto(file[0],file[1],file[2]))

archivo.close




def CalcularPuntosProyecto():
    for i in range(len(listaProyectos)):
        print("Proyecto: " + listaProyectos[i].getTitutlo())
        puntajeTotal = 0
        cantidadDeIntegrantes = ManejadorIntegrantesProyecto.getCantidadDeIntegrantesProyecto(listaProyectos[i].getIdProyecto())
        
        if cantidadDeIntegrantes >= 3:
            puntajeTotal += 10
        else:
            puntajeTotal -= 20
            print("El Proyecto debe tener como mínimo 3 integrantes")
        Director = ManejadorIntegrantesProyecto.BuscarIntegrante(listaProyectos[i].getIdProyecto(),"director")
        
        if Director != NULL:
            if Director.getCategoria() == "I" or Director.getCategoria() == "II":
                puntajeTotal += 10
            else:
                puntajeTotal -= 5
                print("El Director del Proyecto debe tener categoría I o II")
        else:
            print("El Proyecto debe tener un Director")
            puntajeTotal -= 10
        
        Codirector = ManejadorIntegrantesProyecto.BuscarIntegrante(listaProyectos[i].getIdProyecto(),"codirector")
        
        if Codirector != NULL:
            if Codirector.getCategoria() == "I" or Codirector.getCategoria() == "II" or Codirector.getCategoria() == "III":
                puntajeTotal += 10
            else:
                puntajeTotal -= 5
                print("El Codirector del Proyecto debe tener como mínimo categoría III")
        else:
            puntajeTotal -= 10
            print("El Proyecto debe tener un Codirector")
        
        listaProyectos[i].ModificarPuntaje(puntajeTotal)
        print("Puntaje Total: " + str(puntajeTotal))

def HacerRanking():
    listaProyectos.sort()
    print("Ranking: ")
    for i in range(len(listaProyectos)):
        print(listaProyectos[i].getIdProyecto(),listaProyectos[i].getTitutlo(),listaProyectos[i].getPalabrasClave())