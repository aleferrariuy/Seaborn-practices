import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Testing path
# ruta_archivo_df = 'C:\\Users\\agfep\\Documents\\GitHub\\Seaborn-practices\\code\\datasets\\demo.csv' 
ruta_archivo_df = './datasets/demo.csv'

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
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='anio_nacimiento', kde=True, bins=30)
plt.title('Distribución de Nacimientos por Año')
plt.xlabel('Año de Nacimiento')
plt.ylabel('Número de Nacimientos')
plt.grid(axis='y', alpha=0.75)
plt.show()