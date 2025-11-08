import requests
import logging
from sqlalchemy import case, create_engine
import pandas as pd
import pymysql



logging.basicConfig(level=logging.INFO)


API_ALL = "https://restcountries.com/v3.1/all/?fields=name"
PAISES_NOMBRE_OFICIAL = set()
PAISES_NOMBRE_COMUN = set()

PAISES_ERROR_CONSULTA_NOMBRE = set()

PAISES_INFO = list()

def obtener_todos_nombres_paises():
    respuesta = requests.get(API_ALL)
    if respuesta.status_code == 200:
        datos = respuesta.json()
            
        for pais in datos: 
                
            nombre_oficial = pais["name"]["official"]
            PAISES_NOMBRE_OFICIAL.add(nombre_oficial)
                
            nombre_comun = pais["name"]["common"]
            PAISES_NOMBRE_COMUN.add(nombre_comun)

    else :
        print("Error en la consulta")

def consultar_individual_por_nombre_comun_pais(): 

    if len(PAISES_INFO) != len(PAISES_NOMBRE_COMUN):
    
        for nombre in sorted(PAISES_NOMBRE_COMUN):
            pais = nombre
            
            respuesta = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")

            if respuesta.status_code == 200:
                datos = respuesta.json()

                data = {
                    "nombre_oficial": datos[0]["name"]["official"],
                    "nombre_comun": datos[0]["name"]["common"],
                    "monedas": datos[0].get("currencies", None),
                    "capital": datos[0].get("capital", None),
                    "region": datos[0].get("region", None),
                    "subregion": datos[0].get("subregion", None),
                    "idiomas": datos[0].get("languages", None),
                    "poblacion": datos[0].get("population", None),
                    "latitud_capital": datos[0].get("capitalInfo", {}).get("latlng", [0, None])[0],
                    "longitud_capital": datos[0].get("capitalInfo", {}).get("latlng", [None, 0])[1]
                }
                
                if PAISES_INFO.count(data) != len(PAISES_NOMBRE_COMUN):
                    PAISES_INFO.append(data)
                
                logging.info(f"Consultando país: {pais}")
                
            else :
                logging.error(f"Error en la consulta para el país: {pais}")
                PAISES_ERROR_CONSULTA_NOMBRE.add(pais)

        paises_con_error_consulta_nombre_comun()
    else: 
        logging.info("Ya se han consultado y almacenado todos los países.")
    
def paises_con_error_consulta_nombre_comun():
    logging.info("--------------------------------------------------")
    logging.info("Países con error en la consulta por nombre común:")

    for pais in sorted(PAISES_ERROR_CONSULTA_NOMBRE):
        logging.info(pais)
    logging.info(f"Total países con error en la consulta por nombre común: {len(PAISES_ERROR_CONSULTA_NOMBRE)}")


def consultar_un_pais(pais):
    response = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")
    if response.status_code == 200:
        datos = response.json()
        
        data = {
            "nombre_oficial": datos[0]["name"]["official"],
            "nombre_comun": datos[0]["name"]["common"],
            "monedas": datos[0].get("currencies", None),
            "capital": datos[0].get("capital", None),
            "region": datos[0].get("region", None),
            "subregion": datos[0].get("subregion", None),
            "idiomas": datos[0].get("languages", None),
            "poblacion": datos[0].get("population", None),
            "latitud_capital": datos[0].get("capitalInfo", {}).get("latlng", [0, None])[0],
            "longitud_capital": datos[0].get("capitalInfo", {}).get("latlng", [None, 0])[1],
            "capital_info": datos[0].get("capitalInfo", None)    
                    
        }
        
        return data
        
    return None

def obtener_pais_consulta():
    pais = input("Ingresa el nombre del país que deseas consultar:").lower().strip()
    pais_info = consultar_un_pais(pais)
    if pais_info:
        logging.info(f"Información del país '{pais}': {pais_info}")
    else:
        logging.warning(f"No se encontró información para el país: {pais}")
        

def seleccionar_operacion():
    operacion = input_operacion()
    match operacion:
        case 1:
            obtener_pais_consulta()
                
        case 2:
            obtener_todos_nombres_paises()
            consultar_individual_por_nombre_comun_pais()
                
        case _:
            print("Opción no válida")
    
    return operacion

def input_operacion():
    while True:
        try:
            print("Seleccione la operación que desea realizar:")
            print("1. Consultar un país por nombre")
            print("2. Consultar todos los países y obtener sus nombres oficiales y comunes")
            operacion = int(input("Ingrese el número de la operación (1-2): "))
            return operacion
        
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue
            
operacion = seleccionar_operacion()

if operacion == 2:
    """Datos Crudos y Sin Aplanar"""
    logging.info(f"Total Paises con información {len(PAISES_INFO)}")

    df = pd.json_normalize(PAISES_INFO)

    print(df)
    df.to_excel("paises_info.xlsx", index=False)

    """Aplanando Datos y creando conexion a BD MySQL"""

    engine = create_engine('mysql+pymysql://root:123a456b789cdee@localhost:3306/paises')

    for pais in PAISES_INFO: 
        nuevo = {
        "nombre_oficial": pais.get("nombre_oficial"),
        "nombre_comun": pais.get("nombre_comun"),
        "capital": pais.get("capital"),
        "region": pais.get("region"),
        "subregion": pais.get("subregion"),
        "poblacion": pais.get("poblacion"),
        
        
        "latitud_capital": pais.get("capitalInfo", {}).get("latlng", [0, None])[0],
        "longitud_capital": pais.get("capitalInfo", {}).get("latlng", [None, 0])[1]
        
        }


    """
        "monedas": datos[0].get("currencies", None),
        "capital": datos[0].get("capital", None),
        "idiomas": datos[0].get("languages", None),
    """

