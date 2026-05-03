"""
Ejercicio 3: Notaría
Duración: 9 horas (540 minutos, cierre a las 5 PM pero se vacía el sistema)
Llegadas: Exponencial(media=4 minutos)
Recursos: 3 estaciones (asignación, autenticación, emisión)
Enrutamiento: 60% a autenticación, 40% a emisión
Servicios:
  - Asignación: Normal(2, 0.5) minutos
  - Autenticación: Normal(8, 1.5) minutos
  - Emisión: Uniforme[7, 10] minutos
Corridas: 5 semillas diferentes
"""

import simpy
import numpy as np

def cliente_notaria(env, asignacion, autenticacion, emision, rng, registros):
    """
    Simula el proceso de un cliente en la notaría.
    
    Args:
        env: Entorno de SimPy
        asignacion: Recurso para asignación de turnos
        autenticacion: Recurso para autenticación
        emision: Recurso para emisión
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    llegada = env.now
    
    # Etapa 1: Asignación de turnos
    llegada_asig = env.now
    with asignacion.request() as req:
        yield req
        espera_asig = env.now - llegada_asig
        registros['cola_asig'].append(espera_asig)
        
        # Normal(2, 0.5), pero no negativo
        t_servicio = max(0, rng.normal(2, 0.5))
        registros['uso_asig'] += t_servicio
        yield env.timeout(t_servicio)
    
    # Etapa 2: Enrutamiento (60% Autenticación, 40% Emisión)
    prob = rng.random()
    
    if prob <= 0.60:
        # Autenticación de documentos
        llegada_aut = env.now
        with autenticacion.request() as req:
            yield req
            espera_aut = env.now - llegada_aut
            registros['cola_aut'].append(espera_aut)
            
            # Normal(8, 1.5), pero no negativo
            t_servicio = max(0, rng.normal(8, 1.5))
            registros['uso_aut'] += t_servicio
            yield env.timeout(t_servicio)
    else:
        # Emisión de documentos legales
        llegada_emi = env.now
        with emision.request() as req:
            yield req
            espera_emi = env.now - llegada_emi
            registros['cola_emi'].append(espera_emi)
            
            # Uniforme[7, 10]
            t_servicio = rng.uniform(7, 10)
            registros['uso_emi'] += t_servicio
            yield env.timeout(t_servicio)
    
    # Registro del tiempo total en el sistema
    registros['tiempo_sistema'].append(env.now - llegada)


def llegadas_notaria(env, asignacion, autenticacion, emision, rng, registros):
    """
    Genera llegadas de clientes hasta las 5 PM (540 minutos).
    El sistema sigue atendiendo después del cierre hasta vaciar.
    
    Args:
        env: Entorno de SimPy
        asignacion: Recurso para asignación
        autenticacion: Recurso para autenticación
        emision: Recurso para emisión
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    i = 0
    while env.now < 540:  # 9 horas de operación
        tiempo_llegada = rng.exponential(4)  # Media 4 minutos
        # Si la próxima llegada supera el tiempo de cierre, no entra
        if env.now + tiempo_llegada >= 540:
            break
        yield env.timeout(tiempo_llegada)
        i += 1
        env.process(cliente_notaria(env, asignacion, autenticacion, emision, rng, registros))


def ejecutar_simulacion_e3(semilla):
    """
    Ejecuta una corrida de simulación de la notaría.
    
    Args:
        semilla: Semilla para reproducibilidad
        
    Returns:
        Diccionario con métricas de la corrida
    """
    env = simpy.Environment()
    rng = np.random.default_rng(semilla)
    
    # Crear recursos (estaciones)
    asignacion = simpy.Resource(env, capacity=1)
    autenticacion = simpy.Resource(env, capacity=1)
    emision = simpy.Resource(env, capacity=1)
    
    registros = {
        'cola_asig': [],
        'cola_aut': [],
        'cola_emi': [],
        'uso_asig': 0,
        'uso_aut': 0,
        'uso_emi': 0,
        'tiempo_sistema': []
    }
    
    env.process(llegadas_notaria(env, asignacion, autenticacion, emision, rng, registros))
    env.run()  # Corre hasta que se vacíe el sistema
    
    # Calcular tiempo total de simulación (tiempo en que se vacía)
    tiempo_total_sim = env.now
    
    # Cálculos para asignación
    prom_cola_asig = np.mean(registros['cola_asig']) if len(registros['cola_asig']) > 0 else 0
    max_cola_asig = np.max(registros['cola_asig']) if len(registros['cola_asig']) > 0 else 0
    ocup_asig = (registros['uso_asig'] / tiempo_total_sim) * 100
    
    # Cálculos para autenticación
    prom_cola_aut = np.mean(registros['cola_aut']) if len(registros['cola_aut']) > 0 else 0
    max_cola_aut = np.max(registros['cola_aut']) if len(registros['cola_aut']) > 0 else 0
    ocup_aut = (registros['uso_aut'] / tiempo_total_sim) * 100 if registros['uso_aut'] > 0 else 0
    
    # Cálculos para emisión
    prom_cola_emi = np.mean(registros['cola_emi']) if len(registros['cola_emi']) > 0 else 0
    max_cola_emi = np.max(registros['cola_emi']) if len(registros['cola_emi']) > 0 else 0
    ocup_emi = (registros['uso_emi'] / tiempo_total_sim) * 100 if registros['uso_emi'] > 0 else 0
    
    # Tiempo promedio en el sistema
    prom_sistema = np.mean(registros['tiempo_sistema']) if len(registros['tiempo_sistema']) > 0 else 0
    
    # Clientes atendidos
    total_atendidos = len(registros['tiempo_sistema'])
    
    return {
        'semilla': semilla,
        'atendidos': total_atendidos,
        'tiempo_sim': tiempo_total_sim,
        'prom_cola_asig': prom_cola_asig,
        'max_cola_asig': max_cola_asig,
        'ocup_asig': ocup_asig,
        'prom_cola_aut': prom_cola_aut,
        'max_cola_aut': max_cola_aut,
        'ocup_aut': ocup_aut,
        'prom_cola_emi': prom_cola_emi,
        'max_cola_emi': max_cola_emi,
        'ocup_emi': ocup_emi,
        'prom_sistema': prom_sistema
    }


if __name__ == "__main__":
    print("=" * 140)
    print("EJERCICIO 3: NOTARÍA")
    print("=" * 140)
    print(f"{'Semilla':<8} {'Atendidos':<12} {'T. Sim (min)':<14} {'Prom Cola Asig':<16} {'Max Cola Asig':<16} {'Ocup Asig %':<12}")
    print("-" * 140)
    
    resultados = []
    for semilla in range(1, 6):
        res = ejecutar_simulacion_e3(semilla)
        resultados.append(res)
        print(f"{res['semilla']:<8} {res['atendidos']:<12} {res['tiempo_sim']:<14.1f} {res['prom_cola_asig']:<16.2f} "
              f"{res['max_cola_asig']:<16.2f} {res['ocup_asig']:<12.2f}%")
    
    print("-" * 140)
    
    # Estadísticas agregadas para Asignación
    prom_colas_asig = np.array([r['prom_cola_asig'] for r in resultados])
    max_colas_asig = np.array([r['max_cola_asig'] for r in resultados])
    ocup_asig = np.array([r['ocup_asig'] for r in resultados])
    
    # Estadísticas agregadas para Autenticación
    prom_colas_aut = np.array([r['prom_cola_aut'] for r in resultados])
    max_colas_aut = np.array([r['max_cola_aut'] for r in resultados])
    ocup_aut = np.array([r['ocup_aut'] for r in resultados])
    
    # Estadísticas agregadas para Emisión
    prom_colas_emi = np.array([r['prom_cola_emi'] for r in resultados])
    max_colas_emi = np.array([r['max_cola_emi'] for r in resultados])
    ocup_emi = np.array([r['ocup_emi'] for r in resultados])
    
    # Tiempo en sistema
    prom_sistema = np.array([r['prom_sistema'] for r in resultados])
    atendidos = np.array([r['atendidos'] for r in resultados])
    
    print(f"\n{'ANÁLISIS AGREGADO (5 CORRIDAS)':<60}")
    print(f"\nClientes atendidos - Promedio: {np.mean(atendidos):.0f}, Desv. Est.: {np.std(atendidos):.1f}")
    
    print(f"\n{'ESTACIÓN: ASIGNACIÓN DE TURNOS':<60}")
    print(f"  Prom. tiempo en cola: {np.mean(prom_colas_asig):.2f} min (Desv. Est.: {np.std(prom_colas_asig):.2f})")
    print(f"  Máx. tiempo en cola: {np.mean(max_colas_asig):.2f} min (Desv. Est.: {np.std(max_colas_asig):.2f})")
    print(f"  Ocupación: {np.mean(ocup_asig):.2f}% (Desv. Est.: {np.std(ocup_asig):.2f}%)")
    
    print(f"\n{'ESTACIÓN: AUTENTICACIÓN DE DOCUMENTOS':<60}")
    print(f"  Prom. tiempo en cola: {np.mean(prom_colas_aut):.2f} min (Desv. Est.: {np.std(prom_colas_aut):.2f})")
    print(f"  Máx. tiempo en cola: {np.mean(max_colas_aut):.2f} min (Desv. Est.: {np.std(max_colas_aut):.2f})")
    print(f"  Ocupación: {np.mean(ocup_aut):.2f}% (Desv. Est.: {np.std(ocup_aut):.2f}%)")
    
    print(f"\n{'ESTACIÓN: EMISIÓN DE DOCUMENTOS LEGALES':<60}")
    print(f"  Prom. tiempo en cola: {np.mean(prom_colas_emi):.2f} min (Desv. Est.: {np.std(prom_colas_emi):.2f})")
    print(f"  Máx. tiempo en cola: {np.mean(max_colas_emi):.2f} min (Desv. Est.: {np.std(max_colas_emi):.2f})")
    print(f"  Ocupación: {np.mean(ocup_emi):.2f}% (Desv. Est.: {np.std(ocup_emi):.2f}%)")
    
    print(f"\n{'SISTEMA COMPLETO':<60}")
    print(f"  Tiempo promedio en sistema: {np.mean(prom_sistema):.2f} min (Desv. Est.: {np.std(prom_sistema):.2f})")
    
    print("=" * 140)
