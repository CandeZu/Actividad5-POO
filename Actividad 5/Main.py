from Alumno import Alumno
import csv

def imprimir():
    print(" ")
    print("----------MENU------------")
    print("1. Porcentaje de Inasistencia")
    print("2. Modificar cantidad maxima de inasistencias permitidas")
    print("0. Salir")
    print(" ")

def testAlumno(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo,delimiter=',')
        
        for fila in reader:
                nombre = fila[0]
                anio = int(fila[1])
                division = int(fila[2])
                inasistencias = int(fila[3])
                unAlumno = Alumno(nombre,anio,division,inasistencias)
                listaAlumno.append(unAlumno)

def menu():
    band=True
    while band:
        imprimir()
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            anio=int(input("Ingrese anio: "))
            div=int(input("Ingrese division (En número): "))
            print(" ")
            print("ALUMNO \t\t\t\t PORCENTAJE DE INASISTENCIA")
            for i, Alumno in enumerate(listaAlumno):
                
                if Alumno.getInasistencias()>Alumno.getMaximoInasistencias() and Alumno.getAnio()==anio and Alumno.getDivision()==div:
                    print("{}\t\t{}%".format(Alumno.getNombre(),Alumno.getPorcentaje()))
                
        elif opcion==2:
                    nuevo=int(input("Nueva cantidad de inasistencias permitidas: "))
                    Alumno.modificarInasistencias(nuevo)
                    print(" ")
                    print("Cantidad permitida de inasistencias: {}".format(Alumno.getMaximoInasistencias()))

        elif opcion==0:
                    print("Programa finalizado. ")
                    band=False

        else:
                print("Opcion no valida")



if __name__ == '__main__':

    listaAlumno=[]
    testAlumno(listaAlumno)

    menu()