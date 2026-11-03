# 📊 TP Colaborativo: Visualización de Datos en Python (Matplotlib & Seaborn)

**Instituto:** ISTEA — Instituto Superior Tecnológico Empresarial Argentino  
**Carrera:** Tecnicatura Superior en Ciencia de Datos  
**Materia:** Programación 1  
**Profesor:** Juan Pablo Sosa  
**Ciclo Lectivo:** Segundo Cuatrimestre 2026  

---

## 👥 Integrantes del Grupo
- Norberto Ruben Lacoste (*poldev28*)
- *(Completar con los integrantes del grupo)*

---

## 🎯 Descripción del Proyecto

Este repositorio contiene el código práctico desarrollado para la defensa del **Trabajo Práctico Colaborativo**, centrado en la **Visualización de Datos** utilizando las bibliotecas fundamentales del ecosistema de Python: **Matplotlib** y **Seaborn**.

A través de distintos scripts prácticos se demuestra:
1. Construcción de gráficos de líneas y barras desde cero con `matplotlib.pyplot`.
2. Personalización estética avanzada (paletas, tipografías, rotaciones de etiquetas y grillas).
3. Gráficos estadísticos comparativos de alto nivel con `seaborn`.
4. Consumo de datos en vivo desde una **API REST externa (Open-Meteo)** en formato JSON y posterior visualización de temperaturas máximas.

---

## 🛠️ Requisitos e Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/poldev28/tp-visualizacion-datos.git
cd tp-visualizacion-datos
```

### 2. Crear y activar un entorno virtual (recomendado)
```bash
# En Windows:
python -m venv .venv
.venv\Scripts\activate

# En Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

Las dependencias principales son:
- **`matplotlib`**: Generación y renderizado de gráficos 2D.
- **`seaborn`**: Gráficos estadísticos y estilos modernos.
- **`pandas`**: Manejo tabular y soporte para datasets de prueba (`tips`).

---

## 🚀 Estructura de Scripts y Ejecución

| Archivo | Biblioteca | Descripción | Cómo ejecutar |
| :--- | :---: | :--- | :--- |
| **`ejercicio1.py`** | `matplotlib` | Gráfico de líneas con la evolución de la temperatura semanal con marcadores y grilla. | `python ejercicio1.py` |
| **`ejercicio2.py`** | `matplotlib` | Gráfico de barras que compara la cantidad de alumnos por materia con rotación a 45°. | `python ejercicio2.py` |
| **`SEABORN.py`** | `seaborn` | Gráfico de barras comparativo (`barplot`) sobre el dataset `tips` (gasto promedio almuerzo vs cena). | `python SEABORN.py` |
| **`tempmaxPLT.py`** | `urllib` + `matplotlib` | Consulta en tiempo real a la API meteorológica de Buenos Aires y grafica las máximas con etiquetas. | `python tempmaxPLT.py` |

---

## 📄 Documentación Adicional
El informe teórico completo y la presentación formal del proyecto se encuentran en el documento entregable de la materia.
