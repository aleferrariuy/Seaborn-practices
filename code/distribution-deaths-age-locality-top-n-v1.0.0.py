import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Age calc
# Datatype is datetime
df['edad_fallecimiento'] = (df['fecha_fallecimiento'] - df['fecha_nacimiento']).dt.days / 365.25

# Data clean
df_fallecidos = df.dropna(subset=['edad_fallecimiento']).copy()

# Data validation
df_fallecidos_localidad = df_fallecidos.dropna(subset=['localidad_fallecimiento']).copy()

# Cities top 10
top_n_localidades = 10 
localidades_top = df_fallecidos_localidad['localidad_fallecimiento'].value_counts().nlargest(top_n_localidades).index.tolist()

df_fallecidos_localidad_top = df_fallecidos_localidad[df_fallecidos_localidad['localidad_fallecimiento'].isin(localidades_top)]

plt.figure(figsize=(15, 8))
sns.violinplot(x='localidad_fallecimiento', y='edad_fallecimiento', data=df_fallecidos_localidad_top, palette='muted', hue='localidad_fallecimiento', legend=False)
plt.title(f'Distribución de la Edad al Fallecer por Localidades Principales (Top {top_n_localidades})')
plt.xlabel('Localidad de Fallecimiento')
plt.ylabel('Edad al Fallecer')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()