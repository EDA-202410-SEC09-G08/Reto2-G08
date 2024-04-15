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
from DISClib.DataStructures import mapentry as me
assert cf
from datetime import datetime 
from collections import Counter

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
    catalog["dic_req_6"] = {
        2022: {
            "junior": lt.newList(datastructure="SINGLE_LINKED"),
            "mid": lt.newList(datastructure="SINGLE_LINKED"),
            "senior": lt.newList(datastructure="SINGLE_LINKED")
            },
        2023: {
            "junior": lt.newList(datastructure="SINGLE_LINKED"),
            "mid": lt.newList(datastructure="SINGLE_LINKED"),
            "senior": lt.newList(datastructure="SINGLE_LINKED")
            }
        }
    catalog["dic_req_7"] = {
        2022: {
            "01": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "02": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "03": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "04": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "05": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "06": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "07": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "08": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "09": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "10": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "11": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "12": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4)
            },
        2023: {
            "01": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "02": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "03": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "04": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "05": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "06": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "07": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "08": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "09": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "10": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "11": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4),
            "12": mp.newMap(numelements=203564,
                            prime=109345121,
                            maptype= "CHAINING", 
                            loadfactor=4)
            }
        }
    
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
    dic_anios = data_structs["dic_req_6"]
    anio = int(data["published_at"].split("-")[0])
    experticia = data["experience_level"]
    ofertas_exp_anio = dic_anios[anio][experticia]
    lt.addLast(ofertas_exp_anio, data)

    #Vamos a generar la función para el req 7
    dic_anios7 = data_structs["dic_req_7"]
    anio = int(data["published_at"].split("-")[0])
    mes = str(data["published_at"].split("-")[1])
    paises_anio_mes = dic_anios7[anio][mes]
    pais = data["country_code"]
    ciudad = data["city"]
    if not mp.contains(paises_anio_mes, pais): 
        info_pais = {
            "pais": pais,
            "ofertas": lt.newList(datastructure="SINGLE_LINKED"),
            "num_ofertas": 0,
            "ciudades_pais": mp.newMap(numelements=203564,
                                       prime=109345121,
                                       maptype= "CHAINING", 
                                       loadfactor=4)
        }
        lt.addLast(info_pais["ofertas"], data)
        info_pais["num_ofertas"] = lt.size(info_pais["ofertas"])
        if not mp.contains(info_pais["ciudades_pais"], ciudad): 
            ofertas_ciudad_pais = lt.newList(datastructure="SINGLE_LINKED")
            lt.addLast(ofertas_ciudad_pais, data)
            mp.put(info_pais["ciudades_pais"], ciudad, ofertas_ciudad_pais)
        else: 
            ofertas_ciudad_pais = me.getValue(mp.get(info_pais["ciudades_pais"], ciudad))
            lt.addLast(ofertas_ciudad_pais, data)
        mp.put(paises_anio_mes, pais, info_pais)
    else: 
        info_pais = me.getValue(mp.get(paises_anio_mes, pais))
        lt.addLast(info_pais["ofertas"], data)
        info_pais["num_ofertas"] = lt.size(info_pais["ofertas"])
        if not mp.contains(info_pais["ciudades_pais"], ciudad): 
            ofertas_ciudad_pais = lt.newList(datastructure="SINGLE_LINKED")
            lt.addLast(ofertas_ciudad_pais, data)
            mp.put(info_pais["ciudades_pais"], ciudad, ofertas_ciudad_pais)
        else: 
            ofertas_ciudad_pais = me.getValue(mp.get(info_pais["ciudades_pais"], ciudad))
            lt.addLast(ofertas_ciudad_pais, data)

            
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


def req_6(data_structs, numero_ciudades, experticia, anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    dic_anios = data_structs["dic_req_6"]
    #Encuentro la lista de ofertas del año dado con la experticia dada
    ofertas_anio_exp = dic_anios[anio][experticia]
    total_ofertas = lt.size(ofertas_anio_exp)

    #Encuentro el total de empresas que tienen ofertas publicadas en el año dado con la experticia dada
    #Encuentro el total de ciudades que tienen ofertas publicadas en el año dado con la experiencia dada.
    empresas = lt.newList(datastructure="SINGLE_LINKED")
    ciudades = mp.newMap(numelements=17,
                         prime=109345121,
                         maptype="CHAINING",
                         loadfactor=4)
    
    for oferta in lt.iterator(ofertas_anio_exp): 
        empresa = oferta["company_name"]
        ciudad = oferta["city"]
        if not lt.isPresent(empresas, empresa): 
            lt.addLast(empresas, empresa)
        if not mp.contains(ciudades, ciudad): 
            info_ciudad = {
                "nombre": ciudad,
                "pais": oferta["country_code"],
                "ofertas": lt.newList(datastructure="SINGLE_LINKED"),
                "num_ofertas": 0,
                "empresas_ciudad": mp.newMap(numelements=17,
                                             prime=109345121,
                                             maptype="CHAINING",
                                             loadfactor=4),
                "num_empresas": 0,
                "mayor_empresa": ()
                }
            lt.addLast(info_ciudad["ofertas"], oferta)
            info_ciudad["num_ofertas"] = lt.size(info_ciudad["ofertas"])

            if not mp.contains(info_ciudad["empresas_ciudad"], empresa): 
                info_empresa = {
                    "nombre": empresa,
                    "ofertas_empresa": lt.newList(datastructure="SINGLE_LINKED"),
                    "num_ofertas": 0
                }
                lt.addLast(info_empresa["ofertas_empresa"], oferta)
                info_empresa["num_ofertas"] = lt.size(info_empresa["ofertas_empresa"])
                mp.put(info_ciudad["empresas_ciudad"], empresa, info_empresa)
            else: 
                info_empresa = me.getValue(mp.get(info_ciudad["empresas_ciudad"], empresa))
                lt.addLast(info_empresa["ofertas_empresa"], oferta)
                info_empresa["num_ofertas"] = lt.size(info_empresa["ofertas_empresa"])
            mp.put(ciudades, ciudad, info_ciudad)
        else: 
            info_ciudad = me.getValue(mp.get(ciudades, ciudad))
            lt.addLast(info_ciudad["ofertas"], oferta)
            info_ciudad["num_ofertas"] = lt.size(info_ciudad["ofertas"])
            if not mp.contains(info_ciudad["empresas_ciudad"], empresa): 
                info_empresa = {
                    "nombre": empresa,
                    "ofertas_empresa": lt.newList(datastructure="SINGLE_LINKED"),
                    "num_ofertas": 0
                }
                lt.addLast(info_empresa["ofertas_empresa"], oferta)
                info_empresa["num_ofertas"] = lt.size(info_empresa["ofertas_empresa"])
                mp.put(info_ciudad["empresas_ciudad"], empresa, info_empresa)
            else: 
                info_empresa = me.getValue(mp.get(info_ciudad["empresas_ciudad"], empresa))
                lt.addLast(info_empresa["ofertas_empresa"], oferta)
                info_empresa["num_ofertas"] = lt.size(info_empresa["ofertas_empresa"])
    
    total_empresas = lt.size(empresas)
    lista_ciudades = mp.keySet(ciudades)
    total_ciudades = lt.size(lista_ciudades)
    if total_ciudades > numero_ciudades: 
        total_ciudades = numero_ciudades

    #Encuentro la ciudad con mayor cantidad de ofertas y su conteo y la ciudad con menor cantidad de ofertas y su conteo
    max_ofertas_ciu = 0
    min_ofertas_ciu = 203564
    lista_dic_ciudades = lt.newList(datastructure="SINGLE_LINKED") #La lista final
    for ciudad in lt.iterator(lista_ciudades): 
        info_ciudad = me.getValue(mp.get(ciudades, ciudad))
        num_ofertas_ciudad = info_ciudad["num_ofertas"]
        if num_ofertas_ciudad > max_ofertas_ciu: 
            max_ofertas_ciu = num_ofertas_ciudad
            ciudad_max = ciudad
        if num_ofertas_ciudad < min_ofertas_ciu: 
            min_ofertas_ciu = num_ofertas_ciudad
            ciudad_min = ciudad
        lista_empresas_ciudad = mp.keySet(info_ciudad["empresas_ciudad"])
        num_empresas_ciudad = lt.size(lista_empresas_ciudad)
        info_ciudad["num_empresas"] = num_empresas_ciudad
        max_ofertas_emp = 0
        for empresa in lt.iterator(lista_empresas_ciudad): 
            info_empresa = me.getValue(mp.get(info_ciudad["empresas_ciudad"], empresa))
            num_ofertas_empresa = info_empresa["num_ofertas"]
            if num_ofertas_empresa > max_ofertas_emp: 
                max_ofertas_emp = num_ofertas_empresa
                empresa_max = empresa
        mayor_empresa = (empresa_max, max_ofertas_emp)
        info_ciudad["mayor_empresa"] = mayor_empresa
        lt.addLast(lista_dic_ciudades, info_ciudad)
    rta_ciudad_max = (ciudad_max, max_ofertas_ciu)
    rta_ciudad_min = (ciudad_min, min_ofertas_ciu)

    #Ordeno la lista de ciudades por numero de ofertas.
    merg.sort(lista_dic_ciudades, sort_criteria6)
    if lt.size(lista_dic_ciudades) > numero_ciudades: 
        lista_dic_ciudades = lt.subList(lista_dic_ciudades, 1, numero_ciudades)
    for ciudad in lt.iterator(lista_dic_ciudades): 
        ciudad.pop("ofertas")
        ciudad.pop("empresas_ciudad")

    return numero_ciudades, total_empresas, total_ofertas , rta_ciudad_max,  rta_ciudad_min, lista_dic_ciudades


def req_7(data_structs, numero_paises, anio, mes):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    dic_anios = data_structs["dic_req_6"]
    paises_anio_mes = dic_anios[anio][mes]
    lista_paises = mp.keySet(paises_anio_mes)

    #Construyo la lista de paises para las respuestas de la consulta y encuentro el país con más ofertas
    lista_dic_paises = lt.newList(datastructure="SINGLE_LINKED") #La lista de paises final
    max_ofertas_pais = 0
    for pais in lt.iterator(lista_paises): 
        info_pais = me.getValue(mp.get(paises_anio_mes, pais))
        lt.addLast(lista_dic_paises, info_pais) 
        num_ofertas_pais = info_pais["num_ofertas"]
        if num_ofertas_pais > max_ofertas_pais: 
            max_ofertas_pais = num_ofertas_pais
            pais_max = pais
    rta_pais_max = (pais_max, max_ofertas_pais) 

    merg.sort(lista_dic_paises, sort_criteria7)
    if lt.size(lista_dic_paises) > numero_paises: 
        lista_dic_paises = lt.subList(lista_dic_paises, 1, numero_paises)

    #Encuentro el total de ofertas de empleo según las condiciones de la consulta.
    total_ofertas = 0
    total_ciudades = 0
    for pais in lt.iterator(lista_dic_paises): 
        num_ofertas_pais = pais["num_ofertas"]
        total_ofertas += num_ofertas_pais
        mapa_cudades_pais = pais["ciudades_pais"]
        lista_ciudades_pais = mp.keySet(mapa_cudades_pais)
        numero_ciudades_pais = lt.size(lista_ciudades_pais)
        total_ciudades += numero_ciudades_pais

    #Ciudades donde se ofertó en los paises de la consulta. 

    return total_ofertas, total_ciudades, rta_pais_max


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
        if data_1["company_name"] < data_2["company_name"]:
            return True 
    else: 
        return False


def sort_criteria6(data_1, data_2): 
    if data_1["num_ofertas"] > data_2["num_ofertas"]: 
        return True
    elif data_1["num_ofertas"] == data_2["num_ofertas"]:
        if data_1["nombre"] > data_2["nombre"]: 
            return True 
    else: 
        return False
    

def sort_criteria7(data_1, data_2): 
    if data_1["num_ofertas"] > data_2["num_ofertas"]: 
        return True
    else: 
        return False


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
