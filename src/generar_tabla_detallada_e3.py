"""
Genera tabla detallada de resultados del ejercicio 3 con todas las estaciones
"""
import sys
sys.path.insert(0, 'src')

from ejercicio_3_notaria import ejecutar_simulacion_e3
import numpy as np

print("=" * 200)
print("RESULTADOS DETALLADOS POR CORRIDA - EJERCICIO 3: NOTARÍA")
print("=" * 200)

# Header de la tabla completa
print(f"{'Semilla':<8} {'Clientes':<12} {'T.Sim(min)':<12} {'ProColAs':<10} {'MaxColAs':<10} {'ProColAu':<10} {'MaxColAu':<10} {'ProColEm':<10} {'MaxColEm':<10}")
print("-" * 200)

resultados_all = []
for semilla in range(1, 6):
    res = ejecutar_simulacion_e3(semilla)
    resultados_all.append(res)
    print(f"{res['semilla']:<8} {res['atendidos']:<12} {res['tiempo_sim']:<12.1f} {res['prom_cola_asig']:<10.2f} {res['max_cola_asig']:<10.2f} "
          f"{res['prom_cola_aut']:<10.2f} {res['max_cola_aut']:<10.2f} {res['prom_cola_emi']:<10.2f} {res['max_cola_emi']:<10.2f}")

print("=" * 200)
print("\nDATOS LISTOS PARA COPIAR EN LA TABLA MARKDOWN\n")

# Tabla 1: Datos principales
print("TABLA 1: DATOS POR CORRIDA (Copiar en el archivo .md)")
print("|Semilla | Clientes | Tiempo Sim (min) | Prom Cola Asig | Máx Cola Asig | Prom Cola Aut | Máx Cola Aut | Prom Cola Emi | Máx Cola Emi |")
print("|--------|----------|-----------------|---------------|--------------|--------------|-------------|--------------|-------------|")
for res in resultados_all:
    print(f"|{res['semilla']:<7} | {res['atendidos']:<8} | {res['tiempo_sim']:<15.1f} | {res['prom_cola_asig']:<13.2f} | {res['max_cola_asig']:<12.2f} | {res['prom_cola_aut']:<12.2f} | {res['max_cola_aut']:<11.2f} | {res['prom_cola_emi']:<12.2f} | {res['max_cola_emi']:<11.2f} |")
