# Simulaciones de Sistemas de Colas - Modelación y Simulación

Este repositorio contiene tres ejercicios de simulación de eventos discretos usando Python, SimPy y NumPy. Cada ejercicio modela un sistema de colas diferente con características específicas.

## Descripción de los Ejercicios

### Ejercicio 1: Cafetería Universitaria
- **Duración**: 4 horas (240 minutos)
- **Llegadas**: Distribución exponencial con media 3 minutos
- **Servicio**: Distribución uniforme [2, 4] minutos
- **Recurso**: 1 cajero
- **Objetivo**: Analizar tiempos de espera y ocupación del servicio

### Ejercicio 2: Cajero Electrónico
- **Duración**: 24 horas (1440 minutos)
- **Llegadas**: Distribución exponencial con media 4 minutos
- **Servicio**: Distribución uniforme [2, 5] minutos
- **Recurso**: 1 cajero
- **Objetivo**: Realizar 5 corridas con diferentes semillas y calcular promedios y desviaciones estándar

### Ejercicio 3: Notaría
- **Duración**: 9 horas (540 minutos, cierre a las 5 PM)
- **Llegadas**: Distribución exponencial con media 4 minutos
- **Recursos**: 3 estaciones (asignación, autenticación, emisión)
- **Enrutamiento**: 60% a autenticación, 40% a emisión
- **Servicios**:
  - Asignación: Normal(2, 0.5) minutos
  - Autenticación: Normal(8, 1.5) minutos
  - Emisión: Uniforme [7, 10] minutos
- **Objetivo**: Analizar colas, ocupación y tiempos totales en el sistema

## Instalación

### Requisitos
- Python 3.8+
- pip

### Dependencias

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

**Paquetes requeridos:**
- `simpy` - Simulación de eventos discretos
- `numpy` - Operaciones numéricas y generadores aleatorios
- `pandas` - Procesamiento de datos (opcional, para análisis)

## Estructura del Repositorio

```
.
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos a ignorar en git
├── src/
│   ├── ejercicio_1_cafeteria.py         # Simulación de cafetería
│   ├── ejercicio_2_cajero.py            # Simulación de cajero electrónico
│   └── ejercicio_3_notaria.py           # Simulación de notaría
└── resultados/
    ├── ejercicio_1_resultados.md        # Tabla de resultados (cafetería)
    ├── ejercicio_2_resultados.md        # Tabla de resultados (cajero)
    └── ejercicio_3_resultados.md        # Tabla de resultados (notaría)
```

## Cómo Ejecutar

Cada script puede ejecutarse de forma independiente desde la línea de comandos:

```bash
# Ejercicio 1: Cafetería (3 semillas)
python src/ejercicio_1_cafeteria.py

# Ejercicio 2: Cajero (5 semillas)
python src/ejercicio_2_cajero.py

# Ejercicio 3: Notaría (5 semillas, sistema vacío al cierre)
python src/ejercicio_3_notaria.py
```

## Decisiones Técnicas Transversales

### 1. Generadores Aleatorios Aislados
Se utiliza `np.random.default_rng(semilla)` para garantizar:
- **Reproducibilidad**: La misma semilla siempre produce los mismos resultados
- **Aislamiento**: Evita contaminación del estado global de aleatoriedad
- **Independencia**: Cada corrida es completamente independiente

### 2. Monitores de Estado
En lugar de calcular promedios sobre la marcha:
- Se guardan **todos los tiempos individuales** en listas
- Al final de la corrida se calculan: promedio, desviación estándar, máximo, mínimo
- Permite análisis estadístico preciso

### 3. Unidad de Tiempo
- **Todo se simula en minutos**
- Facilita la comparación entre ejercicios
- Alineado con los parámetros del problema

## Métricas Calculadas

### Por Estación/Recurso:
- Tiempo promedio en cola (minutos)
- Tiempo máximo en cola (minutos)
- Tiempo promedio en sistema (minutos)
- Porcentaje de ocupación (%)

### Análisis Multi-Corrida (Ejercicios 2 y 3):
- Promedio de promedios (5 corridas)
- Desviación estándar
- Máximo y mínimo observados

## Reproducibilidad

Para reproducir exactamente los resultados:

1. Usa las mismas semillas: {1, 2, 3} para Ejercicio 1; {1, 2, 3, 4, 5} para Ejercicios 2 y 3
2. Mantén los parámetros de distribución sin cambios
3. Ejecuta en el mismo entorno Python (versión de paquetes)

## Validación de Resultados

Después de ejecutar cada script, verifica:

1. **Número de clientes atendidos**: Coherente con llegadas esperadas
2. **Tiempos no-negativos**: Todos los tiempos deben ser ≥ 0
3. **Ocupación ≤ 100%**: El recurso nunca puede estar más que completamente ocupado
4. **Tiempos sistema ≥ tiempos cola**: Un cliente siempre pasó más o igual tiempo en el sistema que en la cola

## Referencias

- [SimPy Documentation](https://simpy.readthedocs.io/)
- [NumPy Random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
- Teoría de Colas M/M/1 y M/G/1

## Autor
Emmanuel Castaño Sepúlveda
Proyecto de simulación para curso de Modelación y Simulación
