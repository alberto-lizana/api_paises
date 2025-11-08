import pandas as pd
import numpy as np


data = pd.read_csv(r'C:\Users\\La Diva\Desktop\Coneccion API PUBLICA\CURSO_PANDAS\Flota_PRUEBA.csv')

count_rows = data.shape[0]
count_columns = data.shape[1]
rows_columns = data.shape

print(data.head(count_rows))


print(f"El número de filas es: {count_rows}")
print(f"El número de filas y columnas es: {rows_columns}")

print(data.info())
print(data.describe())


# Creando una Serie de Pandas 
Libros = pd.Series(["Ley 50", "Conversaciones Cruciales", 'Habitos atómicos', 'El hombre en busca de sentido', 'El Príncipe'])

print("Todos los libros:")
print(Libros)
print("\n")

print("Libro indice 2:")
print(Libros[2])  # Accediendo al tercer elemento de la Serie
print()

print("Los primeros 3 Libros:")
print(Libros.head(3))  # Mostrando los primeros 3 elementos de la Serie
print("\n")

print("Los últimos 2 Libros:")
print(Libros.tail(2))  # Mostrando los últimos 2 elementos de la Serie
print()

# Creando una Serie de Pandas Con indices personalizados 
Libros_personalizados = pd.Series(["Ley 50", "Conversaciones Cruciales", 'Habitos atómicos', 'El hombre en busca de sentido', 'El Príncipe'], index=["A", "B", "C", "D", "E"])
print(Libros_personalizados)
print("\n")


# Creando una Serie de Pandas a partir de un diccionario 
libros_dict = {
    "01": "Ley 50",
    "02": "Conversaciones Cruciales",
    "03": "Habitos atómicos",
    "04": "El hombre en busca de sentido",
    "05": "El Príncipe"
}

dict_libros_to_serie = pd.Series(libros_dict)
print(dict_libros_to_serie)
print()

# Seleccionando un libro a través del índice  
print(dict_libros_to_serie["03"])
print()

