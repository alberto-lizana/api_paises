import pandas as pd

data = {
    'Producto': ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas', 'Peras'],
    'Precios': [100, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

# En este ejemplo crearemos un dataframe alterno conservando el original
df_modificado = df.set_index('Producto') # Aquí el inplace=False está demás ya que este es el valor por defecto.
print(df_modificado) 
print()

print(df)
print()

# Vamos a dejar como indice al Producto en el DataFrame Original
df.set_index('Producto', inplace=True) # Esto significa vamos a estableces el indice en la columna Producto, e inplace=True sirve para modificar el df original
print(df)
print()


# reindexar
nuevo_orden = ['Uvas', 'Manzanas', 'Melones', 'Naranjas', 'Peras', 'Plátanos']
df_reindexado = df.reindex(nuevo_orden)
print(df_reindexado) # Al no existir melon en la tabla anterior los valores que no existen se pondran como null o NaN

# Para renombrar aquí hacemos una copia renombrada
df_renombrado = df.rename(index={  
    'Manzanas': 'Apples', 
    'Naranjas': 'Oranges'}) # Rename no altera el dataframe principal
print(df_renombrado)
print()

# Para volver a colocar los index
df_reset = df.reset_index()
print(df_reset)
print()


