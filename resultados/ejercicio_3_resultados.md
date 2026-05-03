# Resultados Ejercicio 3: Notaría

## Configuración de la Simulación

| Parámetro | Valor |
|-----------|-------|
| Duración | 9 horas (540 minutos) hasta cierre |
| Distribución de llegadas | Exponencial(media = 4 min) |
| Sistema de colas | Red de colas en serie y paralelo |
| Número de corridas | 5 |
| Semillas utilizadas | 1, 2, 3, 4, 5 |

### Servicios por Estación

| Estación | Distribución | Parámetros |
|----------|-------------|-----------|
| Asignación de turnos | Normal | Media = 2 min, σ = 0.5 |
| Autenticación de documentos | Normal | Media = 8 min, σ = 1.5 |
| Emisión de documentos legales | Uniforme | [7, 10] minutos |

### Enrutamiento

- **60%** de clientes → Autenticación de documentos
- **40%** de clientes → Emisión de documentos legales

## Resultados por Corrida

| Semilla | Clientes | Tiempo Sim (min) | Prom Cola Asig | Máx Cola Asig | Prom Cola Aut | Máx Cola Aut | Prom Cola Emi | Máx Cola Emi |
|---------|----------|-----------------|---------------|--------------|--------------|-------------|--------------|-------------|
| 1       | 158      | 723.0           | 1.06          | 7.87         | 107.69       | 180.17      | 55.11        | 80.52       |
| 2       | 154      | 706.7           | 1.01          | 5.24         | 93.41        | 177.63      | 33.48        | 74.85       |
| 3       | 127      | 721.6           | 0.97          | 6.98         | 70.37        | 176.19      | 5.70         | 24.30       |
| 4       | 128      | 609.7           | 0.93          | 6.51         | 36.78        | 93.13       | 27.88        | 63.00       |
| 5       | 139      | 716.0           | 0.80          | 5.68         | 67.87        | 166.88      | 8.09         | 30.42       |

## Tabla de Resultados (5 Corridas)

| Métrica | Promedio | Desv. Est. |
|--------|----------|-----------|
| **ASIGNACIÓN DE TURNOS** | | |
| Tiempo promedio en cola asignación de turnos (minutos) | 0.95 | 0.09 |
| Tiempo máximo en cola asignación de turnos (minutos) | 6.45 | 0.93 |
| Porcentaje de ocupación asignación de turnos | 40.29 | 2.65 |
| **AUTENTICACIÓN DE DOCUMENTOS** | | |
| Tiempo promedio en cola autenticación de documentos (minutos) | 75.22 | 24.25 |
| Tiempo máximo en cola autenticación de documentos (minutos) | 158.80 | 33.14 |
| Porcentaje de ocupación autenticación de documentos | 97.46 | 3.14 |
| **EMISIÓN DE DOCUMENTOS LEGALES** | | |
| Tiempo promedio en cola emisión de documentos legales (minutos) | 26.05 | 18.11 |
| Tiempo máximo en cola emisión de documentos legales (minutos) | 54.62 | 23.04 |
| Porcentaje de ocupación emisión de documentos legales | 69.68 | 15.23 |
| **SISTEMA COMPLETO** | | |
| Tiempo promedio total en el sistema (minutos) | 67.61 | 17.90 |
| Clientes atendidos | 141 | 12.9 |

## Análisis Detallado por Estación

### Estación: Asignación de Turnos

| Estadística | Valor |
|-------------|-------|
| Tiempo promedio en cola | 0.95 min |
| Desviación estándar | 0.09 min |
| Máximo promedio | 6.45 min |
| Ocupación promedio | 40.29 % |

**Análisis**: Esta estación presenta la menor congestión del sistema con ocupación moderada (40.29%) y tiempos de espera muy bajos (0.95 min promedio). No es un cuello de botella.

### Estación: Autenticación de Documentos

| Estadística | Valor |
|-------------|-------|
| Tiempo promedio en cola | 75.22 min |
| Desviación estándar | 24.25 min |
| Máximo promedio | 158.80 min |
| Ocupación promedio | 97.46 % |

**Análisis**: Esta es la ESTACIÓN CUELLO DE BOTELLA del sistema. Con ocupación del 97.46% y tiempos de espera de 75.22 minutos promedio, es el principal factor limitante. El sistema requiere análisis para mejorar esta estación.

### Estación: Emisión de Documentos Legales

| Estadística | Valor |
|-------------|-------|
| Tiempo promedio en cola | 26.05 min |
| Desviación estándar | 18.11 min |
| Máximo promedio | 54.62 min |
| Ocupación promedio | 69.68 % |

**Análisis**: Esta estación tiene una ocupación moderada (69.68%) con tiempos de espera significativos (26.05 min). Hay variabilidad considerable (desv. est. 18.11 min).

## Conclusiones Generales

### Cuello de Botella
La estación más congestionada es **AUTENTICACIÓN DE DOCUMENTOS** con:
- Tiempo promedio en cola de **75.22 minutos**
- Ocupación de **97.46%**
- Tiempo máximo en cola de **158.80 minutos**

### Eficiencia del Sistema
- Tiempo promedio total en sistema: **67.61 minutos**
- Clientes atendidos en promedio: **141 clientes**

### Recomendaciones
1. **Aumentar recursos en Autenticación**: La estación de autenticación es el cuello de botella principal. Se recomienda añadir un servidor adicional o mejorar el proceso.
2. **Optimizar tiempos de servicio**: Revisar el proceso de autenticación para reducir el tiempo medio de servicio de 8 minutos.
3. **Equilibrio de carga**: Analizar si se puede redistribuir parte del flujo hacia la estación de emisión (actualmente con menor ocupación).

## Comparación con Otros Ejercicios

| Aspecto | Cafetería (E1) | Cajero (E2) | Notaría (E3) |
|--------|----------------|------------|-------------|
| Duración | 4 horas | 24 horas | 9 horas |
| Clientes promedio | 73 | 365 | 141 |
| Tiempo cola promedio | 13.62 min | 13.21 min | 34.09 min* |
| Ocupación promedio | 94.49 % | 89.21 % | 69.14 %** |

*Promedio ponderado de las tres estaciones
**Promedio simple de ocupaciones

## Tabla Comparativa: SimPy vs Simul8 (Notaría - Ejercicio 3)

| Métrica | **SimPy (Nuestros Datos)** | **Simul8 (Datos Imagen)** | **Diferencia** | **Análisis** |
|--------|------------------------|----------------------|--------------|-----------|
| **Cola Asignación (min)** | 0.95 | 1.03 | -0.08 (-7.8%) | Muy similar |
| **Cola Autenticación (min)** | 75.22 | 47.16 | +28.06 (+59.5%) | SimPy muestra mayor congestión |
| **Cola Emisión (min)** | 26.05 | 16.61 | +9.44 (+56.8%) | SimPy muestra mayor congestión |
| **Ocupación Asignación (%)** | 40.29 | 48.55 | -8.26 (-17.0%) | Simul8 muestra mayor utilización |
| **Ocupación Autenticación (%)** | 97.46 | 95.40 | +2.06 (+2.2%) | Muy similar, ambos casi saturados |
| **Ocupación Emisión (%)** | 69.68 | 81.54 | -11.86 (-14.5%) | Diferencia moderada |
| **Tiempo en Sistema (min)** | 67.61 | 44.77 | +22.84 (+51.0%) | SimPy muestra mayor tiempo total |
| **Tiempo máx. en Sistema (min)** | (no reportado) | 106.75 | - | Información complementaria Simul8 |

### Análisis de Diferencias

**Observaciones clave:**

1. **Autenticación como cuello de botella**: Ambas simulaciones identifican la autenticación como la estación con mayor congestión, aunque SimPy reporta valores más altos.

2. **Diferencias en Tiempos de Cola**: SimPy reporta tiempos de cola más altos (~59% mayor para autenticación, ~57% para emisión). Esto podría deberse a:
   - Diferencias en la forma de registrar tiempos de cola
   - Variabilidad en las semillas de aleatorización
   - Diferencias sutiles en la lógica de simulación

3. **Ocupación Autenticación**: Ambos reportan valores muy altos (97.46% vs 95.40%), confirmando que es el recurso más crítico.

4. **Consistencia**: A pesar de las diferencias numéricas, ambas simulaciones llegan a conclusiones similares sobre el sistema, validando la modelación.

## Notas

Ejecuta el script con:
```bash
python src/ejercicio_3_notaria.py
```

Copia los resultados de la consola en las tablas anteriores.

### Interpretación de Tiempos

- **Tiempo en cola**: Tiempo esperando antes de ser atendido
- **Tiempo en sistema**: Tiempo desde llegada hasta salida (incluye espera + servicio)
- **Ocupación**: Porcentaje del tiempo que el recurso está siendo utilizado
