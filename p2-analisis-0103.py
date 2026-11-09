import pandas as pd
import numpy as np 
# Santiago Medrano NC 0103
print("Analisisi de datos Transacciones Santiago Medrano NC = 0103")
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df = pd.DataFrame(transacciones)
print(df)
print("-+-+-+- Agrupar por una sola columna Monto -+-+-+-")
agrupado = df.groupby('Es_Fraude')
print(agrupado)
print("-+-+-+-+- Promedio de fraude -+-+-+-+-")
# Comprobacion de Fraude
print(agrupado['Es_Fraude'].mean())
print("-+-+-+-+- Cantidad maxima de transaccion -+-+-+-+-")
# Maxica cantida de dinero
print(agrupado['Monto'].max())

print("+-+-Santiago Medrano+-+-+Segunda parte+-+0103-+-+-+")
print("Agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
# Multiple aggregation functions
agg_result = agrupado['Monto'].agg(['mean', 'sum', 'max', 'min'])
print(agg_result)
print("agrupacion por vaarias columnas")
print("agregar columna al dataframe")
print("Columna Team --> equipo")
df['Equipo'] = ['A','B','A','B','A','B']

grouped_multi = df.groupby(['Id_Transaccion', 'Equipo'])['Monto'].mean()
print(grouped_multi)