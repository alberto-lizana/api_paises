import pandas as pd

data = {
    "Producto": ["Manzana", "Naranja", "Plátano", "Uva", "Pera"],
    "Precio": [100, 80, 60, 120, 90]
}

df1 = pd.DataFrame(data)
print(df1)
print()

df1.set_index('Producto', inplace=True)
print(df1) # Aquí el index deja de existir y es remplazado por Productos
print()


# Viendo precio de produictos en base al nombre del producto
precio_uva = df1.loc['Uva'] # loc significa que vamos a acceder a la tabla a través del índice que en este caso paso a ser el nobmre del producto
print(precio_uva)
print()

df1.sort_values(by='Precio', ascending=True, inplace=True)
print(df1)
print()


df1.sort_index(ascending=True, inplace=True)
print(df1)
print()


nuevo_orden = ["Uva", "Manzana", "Naranja", "Pera", "Plátano", "Melon"]
df1_reindexado = df1.reindex(nuevo_orden)
print(df1_reindexado) 
print()

index_2 = pd.Index(["Manzana", "Pera", "Melon"])
interseccion = df1.index.intersection(index_2)
print(interseccion)

index_3 = pd.Index(["Manzana", "Pera", "Melon"])
interseccion_3 = df1_reindexado.index.intersection(index_3)
print(interseccion_3)

