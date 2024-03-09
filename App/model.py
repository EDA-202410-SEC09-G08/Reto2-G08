"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.ADT import map as mp
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {}
    catalog["jobs"] = lt.newList()
    catalog['map_req1'] = mp.newMap()
    catalog["map_req2"] = mp.newMap()
    return catalog


# Funciones para agregar informacion al modelo

def add_data_jobs(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["jobs"], data)
    mapa_cod = data_structs["map_req1"]
    codigo = data["country_code"]
    experticia = data["experience_level"]
    if not mp.contains(mapa_cod, codigo):
        mapa_exp = mp.newMap()
        lista = lt.newList()
        mp.put(mapa_cod, codigo, mapa_exp)
        mp.put(mapa_exp, experticia, lista)
        lt.addLast(lista, data)
    
    else: 
        mapa_exp = mp.get(mapa_cod,codigo)["value"]
        if not mp.contains(mapa_exp,experticia):
            lista = lt.newList()
            mp.put(mapa_exp, experticia, lista)
            lt.addLast(lista, data)
        else: 
            lista = mp.get(mapa_exp, experticia)["value"]
            lt.addLast(lista, data)

def add_data_jobs2(data_structs, data):
    lt.addLast(data_structs["jobs"],data)
    mapa_empresa = data_structs["map_req2"]
    empresa = data["company_name"]
    ciudad = data["city"]
    if not mp.contains(mapa_empresa, empresa):
        mapa_ciudad = mp.newMap()
        lista = lt.newList()
        mp.put(mapa_empresa, empresa, ciudad)
        mp.put(mapa_ciudad, ciudad, lista)
        lt.addLast(lista, data)

    else: 
        mapa_ciudad = mp.get(mapa_empresa, empresa)["value"]
        if not mp.contains(mapa_ciudad, ciudad):
            lista = lt.newList()
            mp.put(mapa_ciudad, ciudad, lista)
            lt.addLast(lista, data)
        else:
            lista = mp.get(mapa_ciudad, ciudad)["value"]
            lt.addLast(lista,data)


def data_size_jobs(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["jobs"])



def first_last_jobs(data_structs):
    first = lt.subList(data_structs["jobs"],1,3)
    last = lt.subList(data_structs["jobs"],lt.size(data_structs["jobs"])-2,3)
    rta = lt.newList()
    for element in lt.iterator(first):
        lt.addLast(rta,element)
    for element in lt.iterator(last):
        lt.addLast(rta,element)
    return rta



def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, ofertas, codigo_pais, experticia):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    mapa_cod = data_structs["map_req1"]
    mapa_experticia = mp.get(mapa_cod, codigo_pais)["value"]
    rq1 = mp.get(mapa_experticia, experticia)["value"]
    num_ofertas = lt.size(rq1)
    if lt.size(rq1) > ofertas:
        rq1 = lt.subList(rq1, 1, ofertas)
    return num_ofertas, rq1
    
def req_2(data_structs, ofertas, empresa, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    mapa_empresa = data_structs["map_req2"]
    mapa_ciudad = mp.get(mapa_empresa, empresa)["value"]
    rq2 = mp.get(mapa_ciudad, ciudad)["value"]
    num_ofertas = lt.size(rq2) 
    if lt.size(rq2) > ofertas:
        rq2 = lt.subList(rq2, 1, ofertas)
    return num_ofertas, rq2
    
    

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
