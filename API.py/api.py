import pandas as pd

def obtener_datos_csv(limite_registros, nombre_departamento):
    df = pd.read_csv("C:\\Users\\holat\\Python\\ProyectoAPI\\Casos_positivos_de_COVID-19_en_Colombia.csv", low_memory=False)
    df = df[df['Nombre departamento'] == nombre_departamento][:limite_registros]
    df = df[['Estado', 'Edad', 'Tipo de contagio', 'Nombre municipio', 'Nombre departamento', 'Recuperado']]
    return df


# python C:\\Users\\holat\\Python\\ProyectoAPI\\API.py\main.py 