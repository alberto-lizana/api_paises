import pandas as pd

data = {
    'Producto': ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas', 'Peras'],
    'Precio': [100, 80, 60, 120, 90],
    'Stock': [30, 50, 20, 60, 40]
}

df = pd.DataFrame(data)

# Acceder a la columna precios
precios = df['Precio']
print(precios)

# Métodos indexadores loc e iloc 

# Método 1: loc
# Nos permite acceder basándonos en etiquetas (nombres de filas o columnas).
# Podemos seleccionar un subconjunto de filas y/o columnas usando las etiquetas del eje.
producto_naranjas_loc = df.loc[1, 'Producto']
print(producto_naranjas_loc)

# Aquí, el primer argumento (1) corresponde al índice de la fila.
# El segundo ('Producto') es la columna específica.
# Si solo pusiéramos df.loc[1], obtendríamos toda la fila completa.


# Método 2: iloc
# Nos permite acceder basándonos en posiciones enteras (números).
# También permite seleccionar subconjuntos de filas y/o columnas, pero según su posición numérica.
producto_naranjas_iloc = df.iloc[1, 0]
print(producto_naranjas_iloc)
# Aquí, el primer argumento (1) representa la segunda fila (posición 1, ya que empieza en 0),
# y el segundo (0) corresponde a la primera columna.
# Devuelve el mismo valor que el ejemplo anterior.

# Conclusión:
# 'loc' es más seguro para trabajar, ya que si agregamos o reordenamos filas,
# el índice puede cambiar y 'iloc' podría devolver otro resultado.
# En cambio, 'loc' seguirá accediendo por nombre, no por posición.
# Si las posiciones son fijas y el rendimiento es prioritario (grandes volúmenes de datos),
# 'iloc' es una opción ligeramente más rápida.

"""
🧩 Paso 1: df['Precio'] > 80
    Esto no filtra todavía, solo crea una lista de “verdadero o falso” (booleanos) que indica qué filas cumplen la condición.

🧩 Paso 2: df[ ... ]
    Ahora usamos esa lista de True/False dentro del df[...] para quedarnos solo con las filas que tienen True.
    
"""


# Filtros con condicionales en el dataframe
df_precios_altos = df[df['Precio'] > 80]
print(df_precios_altos)
print()

# Filtros con condicionales en el dataframe con operador &
df_precios_stock = df[(df['Precio'] > 60) & (df['Stock'] > 30)]
print(df_precios_stock)
print()


# Where (Método que recibe la condión)
df_where = df['Precio'].where(df['Precio'] > 80, other=0)
print(df_where)
print()


# Query ()
df_query = df.query('Precio > 80')
print(df_query)
print()