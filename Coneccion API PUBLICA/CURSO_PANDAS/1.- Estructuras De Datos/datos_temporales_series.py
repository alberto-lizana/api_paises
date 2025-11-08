import pandas as pd

# Buscar dato en días 
fechas = pd.date_range(start="2025-01-01", periods=6, freq='D')
valores = [34, 44, 65, 53, 39, 76]
serie_temporal = pd.Series(valores, index=fechas)
print(serie_temporal)
print()

print(serie_temporal['2025-01-03'])
print()

# Por Rango de Fechas
print(serie_temporal['2025-01-01':'2025-01-03'])
print()

# Buscar dato por mes  
fechas = pd.date_range(start="2025-01-01", periods=6, freq='ME')
valores = [34, 44, 65, 53, 39, 76]
serie_temporal = pd.Series(valores, index=fechas)
print(serie_temporal)
print()


print(serie_temporal['2025-05'])
print()


# Por Rango de Fechas 
print(serie_temporal['2025-01':'2025-02'])
print()


data = {
    'Fecha': pd.date_range(start='2025-01-01', periods=6, freq='D'),
    'Ventas': [345, 456, 567, 678, 234, 590]
}

df = pd.DataFrame(data)
print(df)


# Colocando a fechas como index 
df.set_index('Fecha', inplace=True)
print(df)


# Ventas Desplazadas 
df['Ventas_desplazadas'] = df['Ventas'].shift(1) #  Desplazamos en uno las ventas en una nueva columna llamada ventas_desplazadas
df['Cambio_ventas'] = df['Ventas'].diff() # Saca la diferencia entre ventas y ventas_desplazadas es decri esi 2025-01-01 ventas 345 el ventas_desplazadas será NaN 
                                          # Por otro lado, 2025-01-02 de vetnas 456 pasa a ventas_desplazadas 345 y la columna cambio de ventas aqui nos daría un valor igual a 456 - 345 que es 111
                                          # Lo que, en consecuencia, nos mostraría las diferencias de dia a dia en ventas.
print(df)
