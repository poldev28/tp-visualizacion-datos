import matplotlib.pyplot as plt
# Datos simples
dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
temperaturas = [18, 20, 19, 23, 25, 22, 21]

# Crear gráfico de líneas
plt.plot(dias, temperaturas, color="red", marker="o", linestyle="--")


# Títulos y etiquetas
plt.title("Evolución de la Temperatura Semanal", fontsize=14, fontweight="bold")
plt.xlabel("Días de la semana")
plt.ylabel("Temperatura (°C)")
plt.grid(True)


# Mostrar el gráfico
plt.show()