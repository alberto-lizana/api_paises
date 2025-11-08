import pandas as pd

# Función para aplicar descuento
def descuento(precio, porc):
    if porc > 1:
        porc /= 100
        return precio * porc
    return precio * porc

def reinicio_dataframe(data):
    # Reinicio
    return pd.DataFrame(data)

# Datos
data = {
    'Producto': ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas', 'Peras'],
    'Precio': [100, 80, 60, 120, 90]
}

df = pd.DataFrame(data)
print(df)
print()

# Aplicar descuento
df['Precio Descuento'] = df['Precio'].apply(lambda x: descuento(x, 85))
print(df)
print()

# Pasar A Mayúsculas los textos
df['Producto'] = df['Producto'].apply(lambda txt: txt.upper())
print(df)
print()


# Pasar A Minúsculas los textos
df['Producto'] = df['Producto'].apply(lambda txt: txt.lower())
print(df)
print()


# Pasar A Capitalize los textos
df['Producto'] = df['Producto'].apply(lambda txt: txt.capitalize())
print(df)
print()

# Reinicio
df = reinicio_dataframe(data)

# Aplicando Map para cambiar valores de producto a ingles
df['Producto'] = df['Producto'].map({'Manzanas': 'Apples', 'Naranjas': 'Oranges'})
print(df) # Podemos observar que los productos que no están en el diccionario se convierten en NaN
print()

# Reinicio
df = reinicio_dataframe(data)
print(df)
print()

# Para que los valores restantes no queden NaN podemos hacer lo siguiente
mapeo = {'Manzanas': 'Apples', 'Naranjas': 'Oranges'}
df['Producto'] = df['Producto'].map(lambda x: mapeo.get(x, x))
print(df) 
print()

# Reinicio
df = reinicio_dataframe(data)
print(df)
print()

# Uso de applymap para aplicar una función a todo el DataFrame
df = df.applymap(lambda x: x.lower() if type(x) == str else x)
print(df) # Aquí podemos ver que todos los textos en el DataFrame se han convertido a minúsculas ya que la condición exige que el tipo sea str. Esto recorre todo el DataFrame
print()

# Recordar Map sirve para modificar datos y filter para filtrar datos en base a condiciones que debe cumplir el dato.

# columnna de descuento
df['Descuento'] = [10, 15, 10, 20, 5]
print(df) 
print()

# Aplicar descuentos 
df['Precio Descuento'] = df.apply(lambda row: row['Precio'] * (100 - row['Descuento']) / 100 , axis= 1)
print(df)
print()

