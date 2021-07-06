import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 

datos = pd.read_csv('/home/hamza/Documentos/Desarrollo/Python/Trading Google/GOOG.csv')
print(datos.head())

MediaMovilSimple30 = pd.DataFrame()
MediaMovilSimple30['Close'] = datos['Close'].rolling(window = 30).mean()
MediaMovilSimple100 = pd.DataFrame()
MediaMovilSimple100['Close'] = datos['Close'].rolling(window = 100).mean()
print(MediaMovilSimple30[MediaMovilSimple30.index == 100])

data = pd.DataFrame()
data['Google'] = datos['Close']
data['MVS30'] = MediaMovilSimple30['Close']
data['MVS100'] = MediaMovilSimple100['Close']

def Grafica():
    plt.figure(figsize=(10, 5))
    plt.plot(datos['Close'], label='Google Stock')
    plt.plot(MediaMovilSimple30['Close'], label = 'Media Movil 30')
    plt.plot(MediaMovilSimple100['Close'], label = 'Media Movil 100')
    plt.title('Acciones de Google - Precio de sus acciones desde el 2012 - 2021')
    plt.xlabel('1 Ene. 2016 - 21 May. 2020')
    plt.ylabel('Precio de Cierre ($)')
    plt.legend(loc = 'upper left')
    plt.show()

def GraficaVenta():
    plt.figure(figsize=(10, 5))
    plt.plot(data['Google'], label = 'Google', alpha = 0.3)
    plt.plot(data['MVS30'], label = 'MVS30', alpha = 0.3)
    plt.plot(data['MVS100'], label = 'MVS100', alpha = 0.3)
    plt.scatter(data.index, data['Compra'], label = 'Precio de Compra', marker = '^', color = 'green')
    plt.scatter(data.index, data['Venta'], label = 'Precio de Venta', marker = 'v', color = 'red')
    plt.title('Acciones de Google - Precio de sus acciones desde el 2012 - 2021')
    plt.xlabel('1 Ene. 2016 - 21 May. 2020')
    plt.ylabel('Precio de Cierre ($)')
    plt.legend(loc = 'upper left')
    plt.show()

def Calculator(data):
    compra = []
    venta = []
    condicion = 0

    for dia in range(len(data)):
        if data['MVS30'][dia] > data['MVS100'][dia]:
            if condicion!=1:
                compra.append(data['Google'][dia])
                venta.append(np.nan)
                condicion = 1
            else:
                compra.append(np.nan)
                venta.append(np.nan)
        elif data['MVS30'][dia] < data['MVS100'][dia]:
            if condicion != -1:
                venta.append(data['Google'][dia])
                compra.append(np.nan)
                condicion = -1
            else:
                compra.append(np.nan)
                venta.append(np.nan)
        else:
                compra.append(np.nan)
                venta.append(np.nan)
    return(compra, venta)

segn = Calculator(data)
data['Compra'] = segn[0]
data['Venta'] = segn[1]

print(GraficaVenta())