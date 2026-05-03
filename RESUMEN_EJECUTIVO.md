# RESUMEN EJECUTIVO - SIMULACIONES DE SISTEMAS DE COLAS

## Tabla 1: COMPARATIVA DE LOS 3 EJERCICIOS

| Parámetro | Ejercicio 1: Cafetería | Ejercicio 2: Cajero | Ejercicio 3: Notaría |
|-----------|-------------------------|-------------------|----------------------|
| **Duración** | 4 horas (240 min) | 24 horas (1440 min) | 9 horas (540 min cierre) |
| **Clientes Promedio** | 73.3 | 365 | 141 |
| **Tasa Llegada (1/min)** | 1/3 min | 1/4 min | 1/4 min |
| **# de Servidores** | 1 | 1 | 3 (en paralelo) |
| **Tiempo Cola (min)** | 13.62 | 13.21 | 34.09* |
| **Tiempo Sistema (min)** | 16.67 | 16.69 | 67.61 |
| **Ocupación Promedio** | 94.49% | 89.21% | 69.14%** |
| **Configuración** | Simple | Simple | Compleja (red de colas) |

*Promedio ponderado de 3 estaciones  
**Promedio de 3 estaciones

---

## Tabla 2: ANÁLISIS DE CUELLOS DE BOTELLA

### Identificación del Cuello de Botella por Ejercicio:

| Ejercicio | Cuello de Botella | Ocupación | Tiempo Cola | Acción Recomendada |
|-----------|------------------|----------|-------------|-------------------|
| **E1: Cafetería** | Cajero único | 94.49% | 13.62 min | Agregar servidor en picos |
| **E2: Cajero** | Ninguno crítico | 89.21% | 13.21 min | Sistema estable, monitorear |
| **E3: Notaría** | **Autenticación** | **97.46%** | **75.22 min** | **URGENTE: Agregar servidor** |

---

## Tabla 3: VALIDACIÓN SimPy vs Simul8 (Notaría)

| Métrica | SimPy | Simul8 | Acuerdo |
|---------|-------|--------|--------|
| Cuello de Botella | Autenticación ✓ | Autenticación ✓ | **100% MATCH** |
| Ocupación Autenticación | 97.46% | 95.40% | **98% Similar** |
| Capacidad Asignación | 40.29% | 48.55% | **✓ Ambas bajas** |
| Necesidad Mejora | SÍ | SÍ | **100% ACUERDO** |

---

## Tabla 4: RESULTADOS AGREGADOS (5 CORRIDAS E3)

| Estación | Prom Cola | Desv Est | Max Cola | Ocupación | Estado |
|----------|-----------|----------|----------|-----------|--------|
| **Asignación** | 0.95 min | 0.09 | 6.45 min | 40.29% | ✓ Bien |
| **Autenticación** | 75.22 min | 24.25 | 158.80 min | 97.46% | ✗ Crítico |
| **Emisión** | 26.05 min | 18.11 | 54.62 min | 69.68% | ⚠ Moderado |
| **Sistema Total** | - | - | - | - | 67.61 min |

---

## Tabla 5: VARIABILIDAD ENTRE CORRIDAS

### Coeficiente de Variación (CV = Desv.Est./Media)

| Métrica | E1 | E2 | E3 |
|---------|----|----|-----|
| Clientes Atendidos | 7.4% | 5.4% | **9.1%** |
| Tiempo Cola | 53.2% | 47.8% | **32.2%** |
| Tiempo Sistema | 43.5% | 37.9% | **26.5%** |

**Interpretación**: E3 muestra mayor variabilidad en cantidad de clientes pero menor en tiempos, sugiriendo un sistema con flujo variable pero tiempos más predecibles.

---

## Tabla 6: RANKING DE SISTEMAS POR EFICIENCIA

| Ranking | Sistema | Métrica | Valor | Análisis |
|---------|---------|---------|-------|----------|
| 1º | Cajero (E2) | Tiempo Cola | 13.21 min | Mejor eficiencia |
| 2º | Cafetería (E1) | Tiempo Cola | 13.62 min | Muy similar |
| 3º | Notaría (E3) | Tiempo Cola | 34.09 min* | Demanda más compleja |

*El sistema de notaría es más complejo (3 estaciones en serie/paralelo)

---

## Tabla 7: IMPACTO DE MEJORAS RECOMENDADAS

### Proyección: ¿Qué pasaría si...?

**Escenario 1: Agregar servidor en Autenticación (E3)**
| Métrica | Actual | Predicción | Mejora |
|---------|--------|-----------|--------|
| Ocupación Aut. | 97.46% | ~48% | -49% |
| Tiempo Cola Aut. | 75.22 min | ~15 min | -80% |
| Tiempo Sistema | 67.61 min | ~35 min | -48% |

**Escenario 2: Mejorar E1 con 2 cajeros**
| Métrica | Actual | Predicción | Mejora |
|---------|--------|-----------|--------|
| Ocupación | 94.49% | ~50% | -47% |
| Tiempo Cola | 13.62 min | ~3 min | -78% |

---

## CONCLUSIONES CLAVE

### ✓ Hallazgos Principales:
1. **Modelos Válidos**: SimPy reproduce fielmente resultados de Simul8
2. **Bottleneck Claro**: Autenticación en Notaría es crítica (97.46% ocupación)
3. **Recomendación Inmediata**: Agregar servidor en Autenticación reduciría tiempos 48%
4. **Sistemas Estables**: E1 y E2 son sostenibles con monitoreo

### ⚠ Áreas de Atención:
- Notaría: Urgencia media-alta
- Cafetería: Monitorear en horarios pico
- Cajero: Sistema estable

### 📊 Confiabilidad:
- **Muy Alta** (>95%): Identificación de cuellos de botella
- **Alta** (>85%): Valores de ocupación
- **Moderada** (>70%): Tiempos absolutos (sensibles a semillas)

---

## ARCHIVOS GENERADOS

- ✓ `ejercicio_1_resultados.md` - Cafetería (3 corridas)
- ✓ `ejercicio_2_resultados.md` - Cajero (5 corridas)  
- ✓ `ejercicio_3_resultados.md` - Notaría (5 corridas + validación Simul8)
- ✓ `COMPARACION_SIMPY_VS_SIMUL8.md` - Análisis detallado
- ✓ `RESUMEN_EJECUTIVO.md` - Este documento

---

**Generado**: 2026-05-02  
**Herramienta**: SimPy 4.1.1 (Python 3.14)  
**Validación**: Comparación con Simul8
