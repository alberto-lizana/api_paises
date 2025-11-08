import pandas as pd
import numpy as np

""" 
Series de Pandas:
    Una Serie de Pandas es una estructura de datos unidimensional que puede almacenar datos de cualquier tipo (enteros, cadenas, números de punto flotante, objetos de Python, etc.). 
    Cada elemento en una Serie tiene un índice asociado que permite acceder a los datos de manera eficiente.
"""

# A partir de una Lista
serie_lista_motos = pd.Series(["Kawasaki", "Yamaha", "Honda", "Suzuki", "Ducati"])
print(serie_lista_motos)
print()

serie_lista_numeros = pd.Series([1, 2, 3, 4, 5])
print(serie_lista_numeros)
print()

# Con indices personalizados 
serie_lista_indicies_personalizados = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
print(serie_lista_indicies_personalizados)
print()


# Serie a partir de un diccionario
dict_key_value = {
    "A1": "Ferrari",
    "A2": "Lamborghini",
    "A3": "Porsche",
    "A4": "Bugatti",
    "A5": "McLaren"    
}

serie_diccionario_autos = pd.Series(dict_key_value)
print(serie_diccionario_autos)
print()

# Manipular datos en las series y operarciones con ellos 
print(serie_lista_motos[2])  # Accediendo al tercer elemento de la Serie
print()

print(serie_lista_numeros[3] ** 2)
print()

print(serie_lista_indicies_personalizados["d"] + 10)
print()

cubico_numeros = np.power(serie_lista_numeros, 3)
print(cubico_numeros)
print()

cuadreado_numeros = np.power(serie_lista_numeros, 2)
print(cuadreado_numeros)
print()


# MÁXIMA 
print(cubico_numeros.max())
print() 


# MÍNIMA
print(cubico_numeros.min())
print()

# MEDIA 
print(cubico_numeros.median())
print()

# PROMEDIO 
print(cubico_numeros.mean())
print()


# DESVIACIÓN ESTÁNDAR
print(cubico_numeros.std())
print()

# CON OPERADORES 
print(cubico_numeros[cubico_numeros >= 27])
print()


# LOGARITMO NATURAL 
log_cubico_numeros = cubico_numeros.apply(np.log)
print(log_cubico_numeros)


nombres = pd.Series(["Alberto", "Trinidad", "Beatriz", "Daniel", "Carolina"])
edades = pd.Series([31, 7, 23, 45, 30])

datos_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades})
print(datos_personas)

