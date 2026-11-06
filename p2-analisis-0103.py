# Importar librerias
import pandas as pd
import numpy as np 
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

