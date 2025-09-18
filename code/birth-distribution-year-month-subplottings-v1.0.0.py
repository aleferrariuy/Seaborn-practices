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

años_nacimiento = sorted(df['anio_nacimiento'].dropna().unique())

# Subplots num cols
n_cols = 5
n_rows = (len(años_nacimiento) + n_cols - 1) // n_cols

# Picture and subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 6, n_rows * 4), sharey=True)
axes = axes.flatten() 


for i, anio in enumerate(años_nacimiento):
    df_anio = df[df['anio_nacimiento'] == anio]
    nacimientos_por_mes_anio = df_anio['mes_nacimiento'].value_counts().sort_index()

    if not nacimientos_por_mes_anio.empty:
        sns.barplot(x=nacimientos_por_mes_anio.index, y=nacimientos_por_mes_anio.values, ax=axes[i], palette='viridis', hue=nacimientos_por_mes_anio.index, legend=False)

        # Trend
        if len(nacimientos_por_mes_anio) > 1:
            x = nacimientos_por_mes_anio.index.values.reshape(-1, 1)
            y = nacimientos_por_mes_anio.values
            # Numpy
            p = np.polyfit(x.flatten(), y, 2) # polynomial fitting of degree 2
            x_fit = np.linspace(1, 12, 100)
            y_fit = np.polyval(p, x_fit)
            axes[i].plot(x_fit, y_fit, color='red', linestyle='--', label='Tendencia')

        axes[i].set_title(f'Año {int(anio)}')
        axes[i].set_xlabel('Mes')
        axes[i].set_ylabel('Número de Nacimientos')
        
        axes[i].set_xticks(range(1, 13)) 

# Hide null subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()