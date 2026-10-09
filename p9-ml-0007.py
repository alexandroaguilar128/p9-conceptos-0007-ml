# Alexandro Aguilar NC = 0007
import pandas as pd
print(pd.__version__) # Output: 1.5.2
datos1 = {    'distancia_km': [2.5, 4.0, 1.2, 5.8, 3.1],
    'trafico_nivel': [1, 3, 1, 3, 2],
    'edad_repartidor': [22, 35, 19, 28, 40],
    'tiempo_entrega_min': [15, 32, 10, 42, 25]
}
df = pd.DataFrame(datos1)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Programa por Alexandro Aguilar NC = 0007")