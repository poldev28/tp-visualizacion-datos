

# En vez de inventar numeros fijos en una lista, preferimos interactuar con una API de clima en tiempo real 
# para obtener las temperaturas maximas de la ultima semana en Bs As y graficarlas. Para eso usamos la API de Open-Meteo (https://open-meteo.com/).

# Importamos urllib.request(viene con python) para hacer la consulta a la API
import urllib.request
# Importamos json para poder desempaquetar la respuesta de la API, que viene en formato JSON
import json
#Importams matplotlib, libreria estandar para convertir numeros en graficos 2D
import matplotlib.pyplot as plt

# Consultamos la API del Clima
# Coordenadas de Buenos Aires: latitud -34.60, longitud -58.38.  url = nuestro elemento que contendra la direccion de la API con los parametros que necesitamos.
url = "https://api.open-meteo.com/v1/forecast?latitude=-34.6037&longitude=-58.3816&daily=temperature_2m_max&past_days=7&forecast_days=1&timezone=America%2FArgentina%2FBuenos_Aires"
print("Consultando temparaturas maximas de la ultima semana...")

#Respuesta = con request.urlopen hacemos la consulta a la API y guardamos la respuesta en la variable respuesta.
respuesta = urllib.request.urlopen(url)
#datos = json.loads desempaquetamos la respuesta y la guardamos en la variable datos
datos = json.loads(respuesta.read())

# Extraemos las fechas y las temperaturas máximas, las guardamos en variante fechas
fechas = datos["daily"]["time"]                    

#dentro de daily, accedemos a temperature_2m_max y guardamos los valores en la variable temperaturas_max
temperaturas_max = datos["daily"]["temperature_2m_max"]  

# Limpiamos las fechas para que muestre solo día/mes y el grafico quede mas prolijo
fechas_cortas = [f"{f.split('-')[2]}/{f.split('-')[1]}" for f in fechas]
        #La función .split('-') agarra la fecha 2026-10-28 y la corta por los guiones, separándola en 3
        #dejamos afuera el año. Armamos for para aplicar en todas las fechas de la semana

# GRAFICAMOS CON MATPLOTLIB

#creamos el lienzo en blanco donde vamos a trabajar, fon figsize definimos el tamaño del grafico
plt.figure(figsize=(8, 4.5))   #(8 de ancho, 4.5 de alto)

# con plot trazamos la línea uniendo puntos de temperaturas máximas
plt.plot(fechas_cortas, temperaturas_max, marker="o", color="#e74c3c", linewidth=2.5, label="Máxima Diaria")


# Agregamos el número del valor exacto en cada punto rojo con un pequeño for que recorre  las fechas
# y las graba con plt.text, que es la funcion que permite escribir texto en el grafico.
for i in range(len(fechas_cortas)):
    plt.text(fechas_cortas[i], temperaturas_max[i], f"{temperaturas_max[i]}°C", 
             ha="center", fontsize=9, fontweight="bold")

# Configuración estética y títulos
plt.title("Pronóstico de Temperaturas Máximas en Buenos Aires (En Vivo)", fontsize=13, fontweight="bold")
plt.xlabel("Fecha", fontsize=11)
plt.ylabel("Temperatura (°C)", fontsize=11)
plt.ylim(min(temperaturas_max) - 3, max(temperaturas_max) + 4)  # Margen para que se lean bien los números
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(loc="upper left")
# ---------------------------------------------------------
# PASO 4: Mostrar el gráfico interactivo
# ---------------------------------------------------------
plt.show()