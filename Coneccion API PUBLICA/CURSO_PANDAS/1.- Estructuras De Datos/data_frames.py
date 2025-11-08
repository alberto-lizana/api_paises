import pandas as pd

# Crear DataFrame a partir de un diccionario

data = [
    {'Nombre': 'Alberto', 'Edad': 31, 'País': 'Chile'},
    {'Nombre': 'Trinidad', 'Edad': 7, 'País': 'Chile'},
    {'Nombre': 'Martín', 'Edad': -5, 'País': 'Cielo'}
]

df = pd.DataFrame(data)

print("DataFrame creado a partir de un diccionario:")
print(df.head())
print()


# Crear DataFrame a partir de un diccionario de listas
data = {
    'Nombre': ['Alberto', 'Trinidad', 'Martín'],
    'Edad': [31, 7, None],
    'País': ['Chile', 'Chile', None]
}

df2 = pd.DataFrame(data)
print("\nDataFrame creado a partir de un diccionario de listas:")
print(df2.head())
print()

print(df['Nombre'])
print(df2['Edad'])
print()

salarios = pd.Series([4000000, 10000000, None])

df3 =df2.copy()
df3['Salario'] = salarios
print("\nDataFrame con nueva columna 'Salario':")
print(df3)
print()


df2['Salario'] = [4000000, 10000000, -5000000]
print("\nDataFrame con nueva columna 'Salario':")
print(df2)
print()


df2.drop('Salario', axis=1, inplace=True)
print("\nDataFrame después de eliminar la columna 'Salario':")
print(df2)
print()


# Seleccionar filas por posición 
primera_fila = df3.iloc[0]
print("\nPrimera fila del DataFrame:")
print(primera_fila)
print()


# Seleccionar filas por condición 
filas_menores_edad = df3.loc[(df3['Edad'] < 18) & (df3['Edad'] >= 0)]
print("\nFilas donde la edad es menor a 18:")
print(filas_menores_edad)
print()

# Ordenar DataFrame por una columna 
ordenan_mayor_a_menor = df3.sort_values(by='Edad', ascending=True)
print(ordenan_mayor_a_menor)
print()

# Eliminando nulos 
eliminando_filas_con_nulos = df3.dropna()
print(eliminando_filas_con_nulos)
print()

# Rellenando nulos 
fill_nulos_edad = df3.fillna(value= {'Edad' : 20, 'País': 'Chile', 'Salario': 1})
print(fill_nulos_edad)

"""
    ✅ Resumen conceptual:
        Contexto	Sintaxis	Qué significa
        Seleccionar o usar la columna	df3['Edad']	Devuelve la columna como Serie para operar sobre ella
        Asignar valor a la columna	{'Edad': 20}	Indica “columna 'Edad' = 20” en un diccionario

        En el primer caso estamos leyendo o filtrando.
        En el segundo caso estamos diciendo cómo rellenar valores.
"""
