"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control 


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control)



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    ofertas = int(input("Ingrese el numero de ofertas solicitada: "))
    codigo_pais = input("Ingrese el codigo de pais a solicitar: ")
    experticia = input("Ingrese el nivel de experticia solicitada: ")
    rq1 = controller.req_1(control, ofertas, codigo_pais, experticia)
    print("El total de ofertas ofrecidas en ", codigo_pais, " es ", rq1[0][0])
    print("El total de ofertas de trabajo ofrecidas para la condición ", experticia, " es ", rq1[0][1])
    print(tabulate(lt.iterator(rq1[0][2]),headers= "keys", tablefmt="grid"))
    tiempo = f"{rq1[1]:.3f}"
    print("Tiempo: ", tiempo, "ms")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    empresa = input("Ingrese el nombre de la empresa a solicitar: ")
    fecha_inicial = input("Ingrese la fecha inicial solicitada: ")
    fecha_final = input("Ingrese la fecha final solicitada: ")
    rq3 = controller.req_3(control,empresa, fecha_inicial, fecha_final)
    print(("El total de ofertas ofrecidas es "),lt.size(rq3[3]))
    print(("El total de ofertas junior ofrecidas es "),(rq3[0]))
    print(("El total de ofertas mid es "),(rq3[1]))
    print(("El total de ofertas senior es "),(rq3[2]))
    print(tabulate(lt.iterator(rq3[3]),headers= "keys", tablefmt="grid"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    ciudad = input("Ingrese la ciudad a solicitar: ")
    fecha_inicial = input("Ingrese la fecha inicial solicitada: ")
    fecha_final = input("Ingrese la fecha final solicitada: ")
    rq5 = controller.req_5(control, ciudad, fecha_inicial, fecha_final)
    print("El total de ofertas publicadas en ", ciudad, " entre la fecha ", fecha_inicial, " y la fecha ", fecha_final, " es ", rq5[0][0])
    print("El total de empresas que publicaron por lo menos una oferta en ", ciudad, " durante el periodo de consulta es ", rq5[0][1])
    print("La empresa con mayor número de ofertas en la ciudad durante el periodo de consulta es ", rq5[0][2][0], " con ", rq5[0][2][1], " ofertas.")
    print("La empresa con menor número de ofertas en la ciudad durante el periodo de consulta es ", rq5[0][3][0], " con ", rq5[0][3][1], " ofertas.")
    print(tabulate(lt.iterator(rq5[0][4]),headers= "keys", tablefmt="grid"))
    tiempo = f"{rq5[1]:.3f}"
    print("Tiempo: ", tiempo, "ms")

    

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    numero_ciudades = int(input("Ingrese el numero de ciudades a solicitar: "))
    experticia = input("Ingrese el nivel de experticia solicitada: ")
    anio = int(input("Ingrese el año a solicitar: "))
    rq6 = controller.req_6(control, numero_ciudades, experticia, anio)
    print("El total de ciudades que cumplen con las condiciones de la consulta es ", rq6[0][0])
    print("El total de empresas que cumplen con las condiciones de la consulta es ", rq6[0][1])
    print("El total de ofertas publicadas que cumplen con las condiciones de la consulta es ", rq6[0][2])
    print("El nombre de la ciudad con mayor cantidad de ofertas de empleos es ", rq6[0][3][0], " con ", rq6[0][3][1], " ofertas.")
    print("El nombre de la ciudad con menor cantidad de ofertas de empleos es ", rq6[0][4][0], " con ", rq6[0][4][1], " ofertas.")
    print(tabulate(lt.iterator(rq6[0][5]),headers= "keys", tablefmt="grid"))
    tiempo = f"{rq6[1]:.3f}"
    print("Tiempo: ", tiempo, "ms")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    numero_paises = int(input("Ingrese el numero de paises a solicitar: "))
    anio = int(input("Ingrese el año de la consulta: "))
    mes = str(input("Ingrese el mes de la consulta: "))
    rq7 = controller.req_7(control, numero_paises, anio, mes)
    print("El total de ofertas de empleo en los paises de la consulta en ", anio, " en el mes ", mes, " es ", rq7[0][0])
    print("El número de ciudades donde se ofertó en los países resultantes de la consulta es ", rq7[0][1])
    print("El nombre del país con mayor cantidad de ofertas es ", rq7[0][2][0], " con ", rq7[0][2][1], " ofertas")
    print("El nombre de la ciudad con mayor cantidad de ofertas es ", " con ", " ofertas")
    tiempo = f"{rq7[1]:.3f}"
    print("Tiempo: ", tiempo, "ms")


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print("Se han cargado",data[0], "trabajos")
            print(tabulate(lt.iterator(data[1]),headers="keys", tablefmt = "grid"))
            print("Se han cargado",data[2], "tipos de trabajo")
            print(tabulate(lt.iterator(data[3]),headers="keys", tablefmt= "grid"))
            print("Se han cargado",data[4], "multilocaciones")
            print(tabulate(lt.iterator(data[5]),headers="keys", tablefmt= "grid"))
            print("Se han cargado",data[6], "habilidades")
            print(tabulate(lt.iterator(data[7]),headers="keys", tablefmt= "grid"))
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
