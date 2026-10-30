import seaborn as sns
import matplotlib.pyplot as plt
# Cargar el dataset de prueba incorporado en Seaborn
datos = sns.load_dataset("tips")
# Configurar el estilo visual de fondo
sns.set_theme(style="whitegrid")
# Crear gráfico de barras comparativo (Día vs Total de la cuenta, separado por Almuerzo y Cena)
plt.figure(figsize=(7, 4))
sns.barplot(data=datos, x="day", y="total_bill", hue="time", palette="Blues")
# Titulo y etiquetas
plt.title("Gasto Promedio por Día: Almuerzo vs Cena", fontsize=13, fontweight="bold")
plt.xlabel("Día de la semana")
plt.ylabel("Promedio de la cuenta ($)")
# Mostrar el gráfico
plt.show()