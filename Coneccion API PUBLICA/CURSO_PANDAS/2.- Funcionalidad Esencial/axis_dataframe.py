# Axies o ejes de un dataframe
import pandas as pd

data = {
    'Producto': ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas', 'Peras'], 
    'Precio': [100, 80, 60, 120, 90],
    'Stock': [30, 50, 20, 60, 40]
}

df = pd.DataFrame(data)
df.set_index('Producto', inplace=True)
print(df)
print()

# Eliminando una fila
df.drop(index='Plátanos', axis=0, inplace=True) # Borrar Fila
print(df)
print()

# Eliminando una columna
df.drop('Stock', axis=1, inplace=True)
print(df)
print()





