import pandas as pd

# Pon aquí el nombre exacto de tu archivo CSV
archivo = 'Encuesta-Proyecto-USM-_Respuestas_.csv'

df = pd.read_csv(archivo, encoding='utf-8-sig', sep=',', quotechar='"')

print("MAPA DE COLUMNAS PARA TU SCRIPT:\n")
for i, columna in enumerate(df.columns):
    print(f"fila.iloc[{i}]  ->  {columna}")