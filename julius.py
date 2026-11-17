from pathlib import Path
 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
 
# Ejecuta este script desde la carpeta raíz de tu proyecto.
archivo = Path("data/ventas_cafeteria.csv")
carpeta_plots = Path("plots")
carpeta_plots.mkdir(parents=True, exist_ok=True)
 
df = pd.read_csv(archivo)
df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y-%m-%d", errors="raise")
for columna in ["Cantidad", "Precio_Unitario"]:
    df[columna] = pd.to_numeric(df[columna], errors="raise")
if df[["ID", "Fecha", "Cantidad", "Precio_Unitario"]].isna().any().any():
    raise ValueError("Hay datos faltantes en campos necesarios para el cálculo.")
 
df["Ingreso"] = df["Cantidad"] * df["Precio_Unitario"]
 
# Supuesto: cada ID identifica un ticket. Suma sus líneas si tiene varias.
fechas_por_ticket = df.groupby("ID")["Fecha"].nunique()
if fechas_por_ticket.gt(1).any():
    raise ValueError("Un mismo ID aparece en varias fechas; revisa la clave del ticket.")
tickets = df.groupby(["Fecha", "ID"], as_index=False).agg(
    Importe_ticket=("Ingreso", "sum")
)
resumen = (
    tickets.groupby("Fecha")
    .agg(
        Numero_tickets=("ID", "size"),
        Ingreso_diario=("Importe_ticket", "sum"),
        Ticket_promedio=("Importe_ticket", "mean"),
    )
    .sort_index()
    .reset_index()
)
resumen["Ingreso_acumulado"] = resumen["Ingreso_diario"].cumsum()
print(resumen.to_string(index=False, float_format=lambda x: f"{x:.2f}"))
 
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
sns.lineplot(data=resumen, x="Fecha", y="Ticket_promedio", marker="o", ax=axes[0])
axes[0].set(title="Ticket promedio por día", ylabel="Importe por ticket")
sns.lineplot(
    data=resumen, x="Fecha", y="Ingreso_acumulado", marker="o",
    color="#16856b", ax=axes[1]
)
axes[1].set(title="Ingreso acumulado hasta cada día", ylabel="Ingreso acumulado", xlabel="Fecha")
fig.autofmt_xdate(rotation=30)
fig.tight_layout()
salida = carpeta_plots / "ticket_promedio_ingreso_acumulado.png"
fig.savefig(salida, dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"Visualización guardada en: {salida}")