import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Testing path
ruta_archivo_df = 'C:\\Users\\agfep\\Documents\\GitHub\\Seaborn-practices\\code\\datasets\\demo.csv' 
# ruta_archivo_df = './datasets/demo.csv'

try:
    df = pd.read_csv(ruta_archivo_df)
except FileNotFoundError:
    print(f"Error: El archivo {ruta_archivo_df} no se encontró.")
    exit()

df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')
df['fecha_fallecimiento'] = pd.to_datetime(df['fecha_fallecimiento'], errors='coerce')

# ETL...
df['anio_nacimiento'] = df['fecha_nacimiento'].dt.year
df['mes_nacimiento'] = df['fecha_nacimiento'].dt.month
df['anio_fallecimiento'] = df['fecha_fallecimiento'].dt.year
df['mes_fallecimiento'] = df['fecha_fallecimiento'].dt.month

# Plotting...
# Contar nacimientos por mes
nacimientos_por_mes = df['mes_nacimiento'].value_counts().sort_index()

# Visualizar la distribución de nacimientos por mes con gráfico de barras horizontales
plt.figure(figsize=(10, 7))
sns.barplot(x=nacimientos_por_mes.values, y=nacimientos_por_mes.index, orient='h', palette='viridis', hue=nacimientos_por_mes.index, legend=False)
plt.title('Distribución de Nacimientos por Mes')
plt.xlabel('Número de Nacimientos')
plt.ylabel('Mes de Nacimiento')
plt.yticks(nacimientos_por_mes.index, ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
plt.grid(axis='x', alpha=0.75)
plt.show()