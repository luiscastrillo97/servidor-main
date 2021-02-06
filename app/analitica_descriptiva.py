import pandas as pd
import numpy as np
import csv
import datetime

file_name = "data/data_base.csv"


def guardar(data, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_Maximo(datos_pandas, file_name)
    funcion_Minimo(datos_pandas, file_name)
    funcion_Promedio(datos_pandas, file_name)
    funcion_Mediana(datos_pandas, file_name)
    funcion_Desviacion(datos_pandas, file_name)
    funcion_Varianza(datos_pandas, file_name)
    datos_graficar = leer_datos(file_name)
    return datos_graficar

def funcion_Maximo(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    maximo = max(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Maximo", maximo]
    guardar(dato_guardar, file_name)
    
    
def funcion_Minimo(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    minimo = min(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Minimo", minimo]
    guardar(dato_guardar, file_name)

def funcion_Promedio(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    promedio = np.mean(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Promedio", promedio]
    guardar(dato_guardar, file_name)

def funcion_Mediana(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    mediana = np.median(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Mediana", mediana]
    guardar(dato_guardar, file_name)
    

def funcion_Varianza(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    varianza = np.var(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Varianza", varianza]
    guardar(dato_guardar, file_name)

def funcion_Desviacion(datos, file_name):
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    desviacion = np.std(valor_temperatura)
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    dato_guardar = data = [1, date_string, "Desviacion", desviacion]
    guardar(dato_guardar, file_name)

