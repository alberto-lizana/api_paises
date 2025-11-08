import pandas as pd

serie_uno = pd.Series([10, 20, 30], index= ['a', 'b', 'c'])
serie_dos = pd.Series([40, 50, 60, 70], index= ['b', 'c', 'd', 'e'])


print(serie_uno)
print()
print(serie_dos)
print()

resultado = serie_uno + serie_dos
print(resultado) # Aquí el indice es el protagonista, es decir, solo se sumarán los números en los cuales coincide el indice de la serie. Por otro lado, los indices que no se repiten quedan como NaN.




# Para que el problema anterior de NaN no suceda tenemos que aplciar el método add para rellenar los especios vacíos y así en vez de tener not a number por lo menos mantener el número único pertenenciente a la serie en la cual se encuentre algún número.
# Cabe destacar que al utilizar este método se crea una nueva serie. 
resultado_con_fill= serie_uno.add(serie_dos, fill_value=0)
print(resultado_con_fill)
print()

resultado_con_fill_dos = serie_dos.add(serie_uno, fill_value=0)
print(resultado_con_fill_dos) # Como podemos observar en este método no importa el orden en el cual se colocan las series, es decir, rellena tanto a la izquierda como a la derecha.
print()


# Creación de data frame con diccionarios e indices en la misma construcción.
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[1, 2])
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]}, index=[2, 3])

# Al realizar la suma común
resultado = df1 + df2
print(resultado) # Como podemos observar un dataframe requiere mas condiciones para lograr sumarse con otro dataframe. Si bien en una serie consistia en solo tener el mismo índice, en un dataframe requiere que sea mismo indice y misma columna. 5 + 4 = 9
print()


# En DataFrames también podemos utilizar add con fill_value para evitar el NaN, si lo queremos evitar...
resultado = df1.add(df2, fill_value=0)
print(resultado) # Aquí nos damos cuenta de que solo se rellenarán los números que pertenecen a la suma, en otras palabras, si directamente no existe ningun valor en la columna, tanto en el df1 como en el df2, quedará NaN

# fill_value: Fill value entonces nos da un uso bastante cuidadoso ya  que rellenará valores que requieren existencia en algún dataframe en cuestion, en caso de no contar con requerida existencia el resultado de ese índice y columna será igual a NaN.

