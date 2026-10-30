import matplotlib.pyplot as plt

materias = ["Matemática", "Lengua", "Ciencias", "Historia", "Inglés"]
cantidad_alumnos = [30, 25, 28, 22, 27]

plt.bar(materias, cantidad_alumnos, color="skyblue")
plt.title("Distribución de Alumnos por Materia", fontsize=17, fontfamily="Consolas", fontweight="bold")
plt.xlabel("Materias", fontsize=12, fontfamily="Consolas", fontweight="bold")
plt.ylabel("Cantidad de Alumnos", fontsize=12, fontfamily="Consolas", fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()