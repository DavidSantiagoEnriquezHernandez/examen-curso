
# @title Descargar datos
import requests as req

URL = 'https://gist.githubusercontent.com/javierIA/06da309a089278be218daf66e02875ab/raw/d0bfabd94c27ad954cba63683d04d460660387f8/salarios.csv'
file = req.get(URL, allow_redirects=True)

open('salarios.csv', 'wb').write(file.content)

"""## Asegúrate de proporcionar la ruta correcta hacia el archivo CSV o que el archivo esté en la misma ubicación que este notebook.

"""

import pandas as pd

# Cargar los datos en la variable df
df = pd
# Verificar que los datos se hayan cargado correctamente
df = pd.read_csv('salarios.csv')
df['Periodo'] = df['Periodo'].astype(int)

print(df.columns)
# Muestra las primeras 5 filas del DataFrame
print(df.head(5))

# @title Estadistica de daframe

estadisticas_basicas = df.describe()
print("\nEstadísticas básicas del DataFrame:")

print(estadisticas_basicas)

# @title Filtro y seleciona datos
# @markdown Seleciona los datos de la columna periodo mayor a 2018
filtro_periodo =  df['Periodo']> 2018
print("\nFilas donde la Periodo es mayor a 2018:")
print(df[filtro_periodo])

# @title Remplaza la columnas
# @markdown Remplaza el nombre columnas a otras la segundo columna no tiene el nombre, este se refiere al timestre favor actualizar el nombre

print("Columnas antes de la modificación:")
print(df.columns)

# Favor usar el nombre trismetre
# Pista la columna se llama "Unnamed: 1"
new_column = 'trismetre'
df.rename(columns={'Unnamed: 1' : new_column}, inplace=True)

print("\nColumnas después de la modificación:")
print(df.columns)

# @title Calcular el total de ingresos para cada año y período

df['Periodo'] = pd.to_numeric(df['Periodo'], errors='coerce')
total_por_periodo = df.groupby(['trismetre', 'Periodo'])['Total'].sum()
print(total_por_periodo)

"""**Alerta** . No tiene datos nulos"""

valores_nulos = df.isnull().sum()

print("Valores nulos en el DataFrame:")
print(valores_nulos)


import matplotlib.pyplot as plt

# Graficar los ingresos totales por período
periodos = total_por_periodo.index.get_level_values('Periodo')
ingresos_totales = total_por_periodo.values



plt.figure(figsize=(10, 6))
plt.bar(periodos, ingresos_totales)
plt.xlabel('Período')
plt.ylabel('Ingresos Totales')
plt.title('Ingresos Totales por Período')
plt.xticks()
plt.show()

"""# Convierte los salarios a dolares
### Supongamos que el tipo de cambio es 1 dólar = 20 unidades de la moneda local

"""

tipo_cambio = 20
def convertir_a_dolares(salario):
    return salario / tipo_cambio

df['Total_dolares'] = df['Total'].apply(convertir_a_dolares)
df['1_salario_minimo_dolares'] = df['1_salario_minimo'].apply(convertir_a_dolares)
df['2_salario_minimo_dolares'] = df['2_salario_minimo'].apply(convertir_a_dolares)
df['3_salario_minimo_dolares'] = df['3_salario_minimo'].apply(convertir_a_dolares)
df['5_salario_minimo_dolares'] = df['5_salario_minimo'].apply(convertir_a_dolares)

print(df)

# @title Copia el token a en la repuesta de TEAMS
import hashlib

df_string = df.to_string()

# Calcular el hash MD5
md5_hash = hashlib.md5(df_string.encode()).hexdigest()

print("Token del DataFrame:")
print(md5_hash)