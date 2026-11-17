import seaborn as sns
import matplotlib.pyplot as plt

# ==============================================================================
# GRÁFICO CON SEABORN: MAPA DE CALOR CON TOTALES - DATASET TITANIC
# ==============================================================================

def main():
    print("Cargando dataset 'titanic' y generando mapa de calor con totales...")

    # 1. Configurar tema, fondo blanco limpio y un tamaño de letra legible
    sns.set_theme(style="white", font_scale=1.1)

    # 2. Cargar dataset, que ya viene incluido en Seaborn
    df_titanic = sns.load_dataset("titanic")

    # Totales generales del barco ((con 891 pasajeros))
    total_personas = len(df_titanic)
    total_sobrevivientes = int(df_titanic["survived"].sum())

    # 3. Tablas resumen por Grupo (who) y Clase (class)
    orden_grupos = ["woman", "child", "man"]
    orden_clases = ["First", "Second", "Third"]

    # Usando pivot_table, cruzamos dos datos: el grupo contra la clase 
    tabla_pct = df_titanic.pivot_table(
        index="who", columns="class", values="survived", aggfunc="mean", observed=True
    ).reindex(index=orden_grupos, columns=orden_clases) * 100

    tabla_vivos = df_titanic.pivot_table(
        index="who", columns="class", values="survived", aggfunc="sum", observed=True
    ).reindex(index=orden_grupos, columns=orden_clases)

    tabla_totales = df_titanic.pivot_table(
        index="who", columns="class", values="survived", aggfunc="count", observed=True
    ).reindex(index=orden_grupos, columns=orden_clases)

    # 4. Crear etiquetas personalizadas para cada celda: "% \n (vivos / total)"
    etiquetas = tabla_pct.copy().astype(str)
    for fila in orden_grupos:
        for col in orden_clases:
            pct = tabla_pct.loc[fila, col]
            vivos = int(tabla_vivos.loc[fila, col])
            tot = int(tabla_totales.loc[fila, col])
            etiquetas.loc[fila, col] = f"{pct:.1f}%\n({vivos}/{tot})"

    # Renombrar filas y columnas al español
    nombres_filas = {"woman": "Mujeres", "child": "Niños", "man": "Hombres"}
    nombres_cols = {"First": "1ª Clase", "Second": "2ª Clase", "Third": "3ª Clase"}
    tabla_pct = tabla_pct.rename(index=nombres_filas, columns=nombres_cols)

    # 5. Con sns.heatmap(), crear el Mapa de Calor
    fig, ax = plt.subplots(figsize=(9, 6), dpi=110)

    sns.heatmap(
        tabla_pct,               # Matriz con los porcentajes (define el color de cada celda)
        annot=etiquetas,         # Muestra dentro de cada celda nuestros textos personalizados ("% y vivos/total")
        fmt="",                  # Desactiva el formato numérico automático (obligatorio cuando annot lleva texto)
        cmap="YlGnBu",           # Paleta de colores: Yellow-Green-Blue (amarillo para valores bajos, azul oscuro para altos)
        linewidths=2.5,          # Grosor de las líneas que separan los cuadrados entre sí
        linecolor="white",       # Color blanco para las líneas separadoras
        vmin=0,                  # Valor mínimo de la escala de colores (0%)
        vmax=100,                # Valor máximo de la escala de colores (100%)
        cbar_kws={"label": "Tasa de Supervivencia (%)"},  # Agrega el título a la barra de colores de la derecha
        annot_kws={"size": 12, "weight": "bold"},         # Cambia el tamaño (12) y pone en negrita el texto de adentro
        ax=ax                    # Le indica en qué área/cuadro de Matplotlib debe dibujarse el gráfico
    )

    # 6. Título principal y subtítulo con el total de personas
    fig.suptitle(                                       # Coloca el título principal arriba 
        "Supervivencia en el Titanic según Grupo y Clase",  # Texto del título principal
        fontsize=16,                                    # Tamaño de la letra del título
        weight="bold",                                  # Pone el título en negrita
        y=0.96                                          # Posición vertical (0.96 = cerca del borde superior)
    )
    ax.set_title(                                       # Coloca un subtítulo justo encima del mapa de calor
        f"Total analizado: {total_personas} personas ({total_sobrevivientes} sobrevivieron | {total_personas - total_sobrevivientes} fallecieron)",  # Texto dinámico con los totales reales
        fontsize=10.5,                                  # Letra más chica que el título principal
        color="#555555",                                # Color gris oscuro para que no compita con el título
        pad=14                                          # Espacio (separación en puntos) entre el subtítulo y el gráfico
    )
    ax.set_xlabel("")                                   # Borra la etiqueta automática del eje X ("class")
    ax.set_ylabel("")                                   # Borra la etiqueta automática del eje Y ("who")
    ax.tick_params(axis="y", rotation=0)                # Deja horizontales los textos del eje Y (Mujeres, Niños, Hombres)

    plt.tight_layout()                                  # Ajusta automáticamente los márgenes para que no se corte ningún texto
    print("Mostrando gráfico en ventana interactiva...")  # Avisa en la consola que el gráfico está por abrirse
    plt.show()                                          # Abre la ventana interactiva y muestra el gráfico en pantalla

if __name__ == "__main__":
    main()