import requests

API_URL_ES = "https://restcountries.com/v3.1/translation/"
API_SUBREGION = "https://restcountries.com/v3.1/subregion/"
API_REGION = "https://restcountries.com/v3.1/region/"
API_ALL = "https://restcountries.com/v3.1/all/?fields=name"

paises_nombre_oficial = set()
paises_nombre_comun = set()


def buscar_pais():
    pais = input("Ingrese el nombre del país del cual quiere información: ")
    
    respuesta = requests.get(API_URL_ES + pais.strip())
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(datos)
    else :
        print("Error en la consulta")
        

def buscar_subregion():
    subregion = input("Ingrese la subregión de la cual quiere información: ")

    respuesta_subregion = requests.get(API_SUBREGION + subregion.strip())
    if respuesta_subregion.status_code == 200:
        datos_subregion = respuesta_subregion.json()
        print(datos_subregion)
    else :
        print("Error en la consulta de subregión")

def buscar_region():
    region = input("Ingrese la región de la cual quiere información: ")

    respuesta_region = requests.get(API_REGION + region.strip())
    if respuesta_region.status_code == 200:
        datos_region = respuesta_region.json()
        print(datos_region)
    else :
        print("Error en la consulta de región")

def obtener_todos_paises():
    
    respuesta = requests.get(API_ALL)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        for pais in datos: 
            
            nombre_oficial = pais["name"]["official"]
            paises_nombre_oficial.add(nombre_oficial)
            
            nombre_comun = pais["name"]["common"]
            paises_nombre_comun.add(nombre_comun)
            
            
    else :
        print("Error en la consulta")

    print("Nombres comunes de los países:")
    print(paises_nombre_comun)
    print(len(paises_nombre_comun))
    

    

operacion = input("""
Seleccione la operación que desea realizar:
1.- Buscar País
2.- Buscar Subregión 
3.- Buscar Región
4.- Obtener todos los países
                  """)
operacion = int(operacion)


match operacion:
    case 1:
        buscar_pais()
        
    case 2:
        buscar_subregion()

    case 3:
        buscar_region()
        
    case 4:
        obtener_todos_paises()
        
    case _:
        print("Opción no válida")
        
        
    

"""
🌍 Regiones y Subregiones
1️⃣ Africa

Northern Africa

Middle Africa

Southern Africa

Eastern Africa

Western Africa


2️⃣ Americas

Northern America

Central America

Caribbean

South America


3️⃣ Asia

Eastern Asia

Southern Asia

Southeastern Asia

Central Asia

Western Asia


4️⃣ Europe

Northern Europe

Southern Europe

Eastern Europe

Western Europe


5️⃣ Oceania

Australia and New Zealand

Melanesia

Micronesia

Polynesia


6️⃣ Polar

(No tiene subregiones en la API)
"""