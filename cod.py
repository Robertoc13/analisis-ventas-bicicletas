import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. Cargar datos
# =========================
ruta = r"C:\Users\RoCanales\Desktop\ICI\Trimestre 2026\Inteligencia de negocios\Curso cisco\ventas_bicicletas.csv"

df = pd.read_csv(ruta)

print("Datos cargados correctamente ✔")
print(df.head())

# =========================
# 2. Ventas por tipo de bicicleta
# =========================
ventas_tipo = df.groupby("Tipo_Bicicleta")["Cantidad_Vendida"].sum()

plt.figure()
ventas_tipo.plot(kind="bar")
plt.title("Ventas por Tipo de Bicicleta")
plt.ylabel("Cantidad Vendida")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_tipo.png")
plt.close()

# =========================
# 3. Ventas por región
# =========================
ventas_region = df.groupby("Region")["Cantidad_Vendida"].sum()

plt.figure()
ventas_region.plot(kind="bar")
plt.title("Ventas por Región")
plt.ylabel("Cantidad Vendida")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_region.png")
plt.close()

# =========================
# 4. Tendencia en el tiempo
# =========================
df["Fecha"] = pd.to_datetime(df["Fecha"])

ventas_tiempo = df.groupby("Fecha")["Cantidad_Vendida"].sum()

plt.figure()
ventas_tiempo.plot()
plt.title("Tendencia de Ventas en el Tiempo")
plt.ylabel("Cantidad Vendida")
plt.xlabel("Fecha")
plt.tight_layout()
plt.savefig("grafico_tiempo.png")
plt.close()

# =========================
# 5. Mensaje final
# =========================
print("Gráficos generados correctamente ✔")
