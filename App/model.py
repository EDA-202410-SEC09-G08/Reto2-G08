﻿"""
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
from DISClib.DataStructures import mapentry as me
assert cf
from datetime import datetime 

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
    catalog["jobs"] = lt.newList(datastructure="SINGLE_LINKED")
    catalog["employments_types"] = lt.newList()
    catalog["multilocation"] = lt.newList()
    catalog["skills"] = lt.newList()
    catalog['map_req1'] = mp.newMap(numelements=203564,
                                    prime=109345121,
                                    maptype= "CHAINING", 
                                    loadfactor=4)
    catalog["map_req2"] = mp.newMap(numelements=203564,
                                    prime=109345121,
                                    maptype= "CHAINING", 
                                    loadfactor=4)
    catalog["map_req3"] = mp.newMap(numelements=203564,
                                    prime=109345121,
                                    maptype= "CHAINING", 
                                    loadfactor=4)
    catalog["map_req5"] = mp.newMap(numelements=203564, 
                                     prime=109345121,
                                     maptype= "CHAINING", 
                                     loadfactor=4)
    catalog["map_req6"] = mp.newMap(numelements=203564, 
                                     prime=109345121,
                                     maptype= "CHAINING", 
                                     loadfactor=4)
    return catalog


# Funciones para agregar informacion al modelo

def add_data_jobs(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["jobs"], data)

    #Vamos a generar la funcion para req1
    mapa_cod = data_structs["map_req1"]
    codigo = data["country_code"]
    experticia = data["experience_level"]
    if not mp.contains(mapa_cod, codigo):
        map_content = {
            "junior": lt.newList(datastructure="SINGLE_LINKED"),
            "mid": lt.newList(datastructure="SINGLE_LINKED"),
            "senior": lt.newList(datastructure="SINGLE_LINKED")
        }
        lt.addLast(map_content[experticia], data)
        mp.put(mapa_cod, codigo, map_content)
    else: 
        map_content = me.getValue(mp.get(mapa_cod, codigo))
        lt.addLast(map_content[experticia], data)

    #Vamos a generar la funcion para req3
    empresa = data["company_name"]
    mapa_emp = data_structs["map_req3"]
    if not mp.contains(mapa_emp, empresa):
        empresa_particular = mp.newMap()
        ofertas = lt.newList()
        mp.put(empresa_particular, "ofertas", ofertas)
        lt.addLast(ofertas,data)
        mp.put(empresa_particular,"exp_junior",0)
        mp.put(empresa_particular,"exp_mid",0)
        mp.put(empresa_particular,"exp_senior",0)
        mp.put(mapa_emp, empresa,empresa_particular)
        if experticia == "junior":
            expjunior = me.getValue(mp.get(empresa_particular, "exp_junior"))
            mp.put(empresa_particular, "exp_junior",expjunior+1)
        elif experticia == "mid":
            expmid = me.getValue(mp.get(empresa_particular, "exp_mid"))
            mp.put(empresa_particular, "exp_mid",expmid+1)
        else:
            expsenior = me.getValue(mp.get(empresa_particular, "exp_senior"))
            mp.put(empresa_particular, "exp_senior",expsenior+1)
    else: 
        empresa_particular = me.getValue(mp.get(mapa_emp, empresa))
        ofertas = me.getValue(mp.get(empresa_particular, "ofertas"))
        lt.addLast(ofertas,data)
        if experticia == "junior":
            expjunior = me.getValue(mp.get(empresa_particular, "exp_junior"))
            mp.put(empresa_particular, "exp_junior",expjunior+1)
        elif experticia == "mid":
            expmid = me.getValue(mp.get(empresa_particular, "exp_mid"))
            mp.put(empresa_particular, "exp_mid",expmid+1)
        else:
            expsenior = me.getValue(mp.get(empresa_particular, "exp_senior"))
            mp.put(empresa_particular, "exp_senior",expsenior+1)
    
    #Vamos a generar la función para el req 5
    mapa_ciudades = data_structs["map_req5"]
    ciudad = data["city"]
    if not mp.contains(mapa_ciudades, ciudad): 
        ofertas_ciudad = lt.newList(datastructure="SINGLE_LINKED")
        lt.addLast(ofertas_ciudad, data)
        mp.put(mapa_ciudades, ciudad, ofertas_ciudad)
    else: 
        ofertas_ciudad = me.getValue(mp.get(mapa_ciudades, ciudad))
        lt.addLast(ofertas_ciudad, data)

    #Vamos a generar la función para el req 6
            
def add_data_employments_types(data_structs,data):
    lt.addLast(data_structs["employments_types"],data)
    
def add_data_multilocation(data_structs, data):
    lt.addLast(data_structs["multilocation"],data)

def add_data_skills(data_structs, data):
    lt.addLast(data_structs["skills"],data)


def data_size_jobs(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["jobs"])

def data_size_employments_types(data_structs):
    return lt.size(data_structs["employments_types"])

def data_size_multilocation(data_structs):
    return lt.size(data_structs["multilocation"])

def data_size_skills(data_structs):
    return lt.size(data_structs["skills"])

def first_last_jobs(data_structs):
    first = lt.subList(data_structs["jobs"],1,3)
    last = lt.subList(data_structs["jobs"],lt.size(data_structs["jobs"])-2,3)
    rta = lt.newList()
    for element in lt.iterator(first):
        lt.addLast(rta,element)
    for element in lt.iterator(last):
        lt.addLast(rta,element)
    return rta

def first_last_employments(data_structs):
    first = lt.subList(data_structs["employments_types"],1,3)
    last = lt.subList(data_structs["employments_types"],lt.size(data_structs["employments_types"])-2,3)
    rta = lt.newList()
    for element in lt.iterator(first):
        lt.addLast(rta,element)
    for element in lt.iterator(last):
        lt.addLast(rta,element)
    return rta

def first_last_multilocation(data_structs):
    first = lt.subList(data_structs["multilocation"],1,3)
    last = lt.subList(data_structs["multilocation"], lt.size(data_structs["multilocation"])-2,3)
    rta = lt.newList()
    for element in lt.iterator(first):
        lt.addLast(rta,element)
    for element in lt.iterator(last):
        lt.addLast(rta,element)
    return rta

def first_last_skills(data_structs):
    first = lt.subList(data_structs["skills"],1,3)
    last = lt.subList(data_structs["skills"], lt.size(data_structs["multilocation"])-2,3)
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
    map_content = me.getValue(mp.get(mapa_cod, codigo_pais))
    total_ofertas_pais =  lt.size(map_content["junior"]) + lt.size(map_content["mid"]) + lt.size(map_content["senior"])
    rq1 = map_content[experticia]
    num_ofertas = lt.size(map_content[experticia])

    #ordeno la lista de ofertas por fecha, en orden cronológico
    merg.sort(rq1, sort_criteria1)
    if num_ofertas > ofertas: 
        rq1 = lt.subList(map_content[experticia], lt.size(map_content[experticia]) - ofertas + 1, ofertas)
    for oferta in lt.iterator(rq1): 
        oferta.pop("street")
        oferta.pop("address_text")
        oferta.pop("marker_icon")
        oferta.pop("company_url")
        oferta.pop("remote_interview")
        oferta.pop("id")
        oferta.pop("display_offer")

    return total_ofertas_pais, num_ofertas, rq1

    
def req_2(data_structs, ofertas, empresa, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass
    
    

def req_3(data_structs,nombre_empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    mapa3 = data_structs["map_req3"]
    mapa_empresa = mp.get(mapa3, nombre_empresa)["value"]
    ofertas = mp.get(mapa_empresa, "ofertas")["value"]
    ofertas_fecha = lt.newList()
    junior = 0
    mid = 0
    senior = 0
    fecha_inicial = datetime.strptime(fecha_inicial,"%Y-%m-%d")
    fecha_final = datetime.strptime(fecha_final,"%Y-%m-%d")
    for oferta in lt.iterator(ofertas): 
        fecha = datetime.strptime(oferta["published_at"].split("T")[0],"%Y-%m-%d")
        if fecha_inicial <= fecha and fecha <= fecha_final:
            lt.addLast(ofertas_fecha,oferta)
            experticia = oferta["experience_level"]
            if experticia == "junior":
                junior +=1
            elif experticia == "mid":
                mid +=1
            else:
                senior +=1
    merg.sort(ofertas_fecha, sort_criteria3)
    return junior, mid, senior, ofertas_fecha



def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs, ciudad, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    mapa_ciudades = data_structs["map_req5"]
    ofertas_ciudad_seleccionada = me.getValue(mp.get(mapa_ciudades, ciudad))
    fecha_inicial = datetime.strptime(fecha_inicial,"%Y-%m-%d")
    fecha_final = datetime.strptime(fecha_final,"%Y-%m-%d")

    #Encuentro el total de ofertas publicadas en la ciudad en el periodo de consulta.
    ofertas_ciudad_tiempo = lt.newList(datastructure="SINGLE_LINKED")
    for oferta in lt.iterator(ofertas_ciudad_seleccionada): 
        fecha_oferta = datetime.strptime(oferta["published_at"].split("T")[0],"%Y-%m-%d")
        if fecha_inicial <= fecha_oferta and fecha_oferta <= fecha_final:
            lt.addLast(ofertas_ciudad_tiempo, oferta)
    total_ofertas = lt.size(ofertas_ciudad_tiempo)

    #Encuentro el total de empresas que publicaron por lo menos una oferta en la ciudad de consulta.
    empresas_ciudad_tiempo = mp.newMap(numelements=203564,
                                       prime=109345121,
                                       maptype="CHAINING",
                                       loadfactor=4)
    for oferta in lt.iterator(ofertas_ciudad_tiempo): 
        empresa = oferta["company_name"]
        if not mp.contains(empresas_ciudad_tiempo, empresa): 
            ofertas_empresa = lt.newList(datastructure="SINGLE_LINKED")
            lt.addLast(ofertas_empresa, oferta)
            mp.put(empresas_ciudad_tiempo, empresa, ofertas_empresa)
        else: 
            ofertas_empresa = me.getValue(mp.get(empresas_ciudad_tiempo, empresa))
            lt.addLast(ofertas_empresa, oferta)
    llaves = mp.keySet(empresas_ciudad_tiempo)
    total_empresas = lt.size(llaves)

    #Empresa con mayor número de ofertas y su conteo. Empresa con menor número de ofertas (al menos una) y su conteo.
    max_ofertas = 0
    min_ofertas = 203564
    for empresa in lt.iterator(llaves): 
        num_ofertas_empresa = lt.size(me.getValue(mp.get(empresas_ciudad_tiempo, empresa)))
        if num_ofertas_empresa > max_ofertas: 
            max_ofertas = num_ofertas_empresa
            empresa_max = empresa
        if num_ofertas_empresa < min_ofertas: 
            min_ofertas = num_ofertas_empresa
            empresa_min = empresa
    rta_empresa_max = (empresa_max, max_ofertas)
    rta_empresa_min = (empresa_min, min_ofertas)

    #El listado de ofertas publicadas ordenadas cronológicamente por fecha y nombre de la empresa. 
    #Fecha de publicación de la oferta, Título de la oferta, Nombre de la empresa de la oferta, 
    #Tipo de lugar de trabajo de la oferta, Tamaño de la empresa de la oferta, Tipo de lugar de trabajo de la oferta
    merg.sort(ofertas_ciudad_tiempo, sort_criteria5)
    for oferta in lt.iterator(ofertas_ciudad_tiempo): 
        oferta.pop("street")
        oferta.pop("address_text")
        oferta.pop("marker_icon")
        oferta.pop("company_url")
        oferta.pop("experience_level")
        oferta.pop("remote_interview")
        oferta.pop("open_to_hire_ukrainians")
        oferta.pop("id")
        oferta.pop("display_offer")

    return total_ofertas, total_empresas, rta_empresa_max, rta_empresa_min, ofertas_ciudad_tiempo


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

def sort_criteria1(data_1, data_2): 
    if datetime.strptime(data_1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")<datetime.strptime(data_2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") :
        return True
    else: 
        return False


def sort_criteria3(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    
    if datetime.strptime(data_1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")<datetime.strptime(data_2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") :
        
        return True
    elif datetime.strptime(data_1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") == datetime.strptime(data_2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ"):
        if data_1["country_code"]< data_2["country_code"]:
            return True 
    else: 
        return False
    

def sort_criteria5(data_1, data_2): 
    if datetime.strptime(data_1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")<datetime.strptime(data_2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") :
        
        return True
    elif datetime.strptime(data_1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") == datetime.strptime(data_2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ"):
        if data_1["company_name"]< data_2["company_name"]:
            return True 
    else: 
        return False


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
