# Resultados Ejercicio 2: Cajero Electrónico

## Configuración de la Simulación

| Parámetro | Valor |
|-----------|-------|
| Duración | 24 horas (1440 minutos) |
| Distribución de llegadas | Exponencial(media = 4 min) |
| Distribución de servicio | Uniforme[2, 5] minutos |
| Número de cajeros | 1 |
| Número de corridas | 5 |
| Semillas utilizadas | 1, 2, 3, 4, 5 |

## Resultados por Corrida

| Semilla | Clientes Atendidos | Prom. Tiempo en Cola (min) | Desv. Est. Cola | Prom. Tiempo Sistema (min) | Desv. Est. Sistema | Ocupación (%) |
|---------|-------------------|--------------------------|-----------------|---------------------------|------------------|---------------|
| 1       | 357                | 10.89                    | 8.95            | 14.34                     | 8.95             | 87.05         |
| 2       | 394                | 25.35                    | 16.85           | 28.86                     | 16.88            | 96.69         |
| 3       | 348                | 8.08                     | 8.65            | 11.58                     | 8.64             | 84.93         |
| 4       | 345                | 8.71                     | 7.61            | 12.25                     | 7.74             | 84.93         |
| 5       | 383                | 13.01                    | 9.33            | 16.43                     | 9.33             | 92.44         |

## Análisis Agregado (5 Corridas)

### Tiempo en Cola

| Estadística | Valor |
|-------------|-------|
| Promedio de promedios | 13.21 min |
| Desviación estándar | 6.32 min |
| Mínimo observado | 8.08 min |
| Máximo observado | 25.35 min |

### Tiempo en Sistema

| Estadística | Valor |
|-------------|-------|
| Promedio de promedios | 16.69 min |
| Desviación estándar | 6.32 min |
| Mínimo observado | 11.58 min |
| Máximo observado | 28.86 min |

### Ocupación del Cajero

| Estadística | Valor |
|-------------|-------|
| Promedio | 89.21 % |
| Desviación estándar | 4.64 % |

### Clientes Atendidos

| Estadística | Valor |
|-------------|-------|
| Promedio | 365 clientes |
| Desviación estándar | 19.6 clientes |

## Conclusiones

- En 24 horas, el cajero electrónico atiende aproximadamente **365 clientes** en promedio.
- El tiempo de espera promedio es de **13.21 minutos**.
- La ocupación promedio del cajero es **89.21%**, indicando un sistema altamente utilizado.
- La variabilidad entre corridas es **moderada**, con desv. est. de 6.32 minutos para tiempos en cola.

## Comparación con Cafetería (Ejercicio 1)

- **Intensidad del servicio**: Cajero [mayor/menor] tráfico que cafetería
- **Tiempo promedio de espera**: [Análisis comparativo]
- **Ocupación**: [Análisis comparativo]

## Notas

Ejecuta el script con:
```bash
python src/ejercicio_2_cajero.py
```

Copia los resultados de la consola en las tablas anteriores.
