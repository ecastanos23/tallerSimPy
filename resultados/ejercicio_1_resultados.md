# Resultados Ejercicio 1: Cafetería Universitaria

## Configuración de la Simulación

| Parámetro | Valor |
|-----------|-------|
| Duración | 4 horas (240 minutos) |
| Distribución de llegadas | Exponencial(media = 3 min) |
| Distribución de servicio | Uniforme[2, 4] minutos |
| Número de cajeros | 1 |
| Semillas utilizadas | 1, 2, 3 |

## Resultados por Corrida

| Semilla | Clientes Atendidos | Tiempo Promedio en Cola (min) | Tiempo Promedio en Sistema (min) | Ocupación Cajero (%) | Cola Máxima |
|---------|-------------------|------------------------------|----------------------------------|----------------------|-------------|
| 1       | 75                | 20.40                        | 23.46                            | 98.32                | 13          |
| 2       | 79                | 16.91                        | 19.94                            | 100.52               | 12          |
| 3       | 66                | 3.56                         | 6.61                             | 84.64                | 4           |

## Análisis Agregado

| Métrica | Promedio | Desviación Estándar | Mínimo | Máximo |
|---------|----------|-------------------|--------|--------|
| Clientes atendidos | 73.3 | 5.4 | 66 | 79 |
| Tiempo en cola (min) | 13.62 | 7.25 | 3.56 | 20.40 |
| Tiempo en sistema (min) | 16.67 | 7.26 | 6.61 | 23.46 |
| Ocupación cajero (%) | 94.49 | 7.03 | 84.64 | 100.52 |

## Conclusiones

- La cafetería atiende aproximadamente **73 clientes** en 4 horas en promedio.
- El tiempo de espera promedio en la cola es de **13.62 minutos**.
- El cajero mantiene una ocupación de **94.49%** durante el período de operación.
- La variabilidad entre corridas es **moderada** (desv. est. de 7.3 para tiempos en cola), indicando sensibilidad a las semillas.

## Notas

Ejecuta el script con:
```bash
python src/ejercicio_1_cafeteria.py
```

Copia los resultados de la consola en las tablas anteriores.
