import os
import pandas as pd


def obtener_datos_csv(lim, num):
    df = pd.read_csv("C:\\Users\\holat\\Python\\ProyectoAPI\\Casos_positivos_de_COVID-19_en_Colombia.csv", low_memory=False)
    df = df[df['Nombre departamento'] == num][:lim]
    return df




def atencion():
    num = input("Ingrese el nombre del departamento a consultar: ")
    while True:
        try:
            lim = int(input("Ingrese el número de registros deseados: "))
            if lim < 1000:
                break
            print("El número de registros debe ser menor a 1000")
        except ValueError:
            print("El número de registros debe ser un número entero")
    df = obtener_datos_csv(lim, num.upper())
    df = df[["Estado", "Edad", "Tipo de contagio", "Nombre municipio", "Nombre departamento", "Recuperado"]]
    print(df.to_string(index=False))
    return num, lim 
    
    
