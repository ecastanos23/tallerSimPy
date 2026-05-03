"""
Ejercicio 2: Cajero Electrónico
Duración: 24 horas (1440 minutos)
Llegadas: Exponencial(media=4 minutos)
Servicio: Uniforme[2, 5] minutos
Recurso: 1 cajero
Corridas: 5 semillas diferentes
"""

import simpy
import numpy as np

def cliente_cajero(env, cajero, rng, registros):
    """
    Simula el proceso de un cliente en el cajero.
    
    Args:
        env: Entorno de SimPy
        cajero: Recurso compartido (servidor)
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    llegada = env.now
    
    with cajero.request() as req:
        yield req
        tiempo_espera = env.now - llegada
        registros['tiempos_cola'].append(tiempo_espera)
        
        # Servicio uniforme [2, 5] minutos
        tiempo_servicio = rng.uniform(2, 5)
        registros['tiempo_uso_cajero'] += tiempo_servicio
        yield env.timeout(tiempo_servicio)
        
        # Tiempo total en el sistema
        tiempo_sistema = env.now - llegada
        registros['tiempos_sistema'].append(tiempo_sistema)


def llegadas_cajero(env, cajero, rng, registros):
    """
    Genera llegadas de clientes con distribución exponencial.
    
    Args:
        env: Entorno de SimPy
        cajero: Recurso compartido
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    i = 0
    while env.now < 1440:  # 24 horas
        tiempo_llegada = rng.exponential(4)  # Media 4 minutos
        yield env.timeout(tiempo_llegada)
        if env.now < 1440:  # Solo crear cliente si no ha pasado el cierre
            i += 1
            env.process(cliente_cajero(env, cajero, rng, registros))


def ejecutar_simulacion_e2(semilla):
    """
    Ejecuta una corrida de simulación del cajero.
    
    Args:
        semilla: Semilla para reproducibilidad
        
    Returns:
        Diccionario con métricas de la corrida
    """
    env = simpy.Environment()
    rng = np.random.default_rng(semilla)
    cajero = simpy.Resource(env, capacity=1)
    
    registros = {
        'tiempos_cola': [],
        'tiempos_sistema': [],
        'tiempo_uso_cajero': 0
    }
    
    env.process(llegadas_cajero(env, cajero, rng, registros))
    env.run(until=1440)
    
    total_atendidos = len(registros['tiempos_sistema'])
    prom_cola = np.mean(registros['tiempos_cola']) if total_atendidos > 0 else 0
    desv_cola = np.std(registros['tiempos_cola']) if total_atendidos > 0 else 0
    max_cola = np.max(registros['tiempos_cola']) if total_atendidos > 0 else 0
    
    prom_sist = np.mean(registros['tiempos_sistema']) if total_atendidos > 0 else 0
    desv_sist = np.std(registros['tiempos_sistema']) if total_atendidos > 0 else 0
    max_sist = np.max(registros['tiempos_sistema']) if total_atendidos > 0 else 0
    
    ocupacion = (registros['tiempo_uso_cajero'] / 1440) * 100
    
    return {
        'semilla': semilla,
        'atendidos': total_atendidos,
        'prom_cola': prom_cola,
        'desv_cola': desv_cola,
        'max_cola': max_cola,
        'prom_sistema': prom_sist,
        'desv_sistema': desv_sist,
        'max_sistema': max_sist,
        'ocupacion': ocupacion
    }


if __name__ == "__main__":
    print("=" * 110)
    print("EJERCICIO 2: CAJERO ELECTRÓNICO")
    print("=" * 110)
    print(f"{'Semilla':<8} {'Atendidos':<12} {'Prom. Cola':<12} {'Desv. Cola':<12} {'Prom. Sistema':<14} {'Desv. Sistema':<14} {'Ocupación':<12}")
    print("-" * 110)
    
    resultados = []
    for semilla in range(1, 6):
        res = ejecutar_simulacion_e2(semilla)
        resultados.append(res)
        print(f"{res['semilla']:<8} {res['atendidos']:<12} {res['prom_cola']:<12.2f} {res['desv_cola']:<12.2f} "
              f"{res['prom_sistema']:<14.2f} {res['desv_sistema']:<14.2f} {res['ocupacion']:<12.2f}%")
    
    # Estadísticas agregadas de las 5 corridas
    print("-" * 110)
    
    prom_colas = np.array([r['prom_cola'] for r in resultados])
    prom_sistemas = np.array([r['prom_sistema'] for r in resultados])
    ocupaciones = np.array([r['ocupacion'] for r in resultados])
    atendidos = np.array([r['atendidos'] for r in resultados])
    
    print(f"\n{'ANÁLISIS AGREGADO (5 CORRIDAS)':<50}")
    print(f"Clientes atendidos - Promedio: {np.mean(atendidos):.0f}, Desv. Est.: {np.std(atendidos):.1f}")
    print(f"\nTiempo en cola:")
    print(f"  Promedio de promedios: {np.mean(prom_colas):.2f} minutos")
    print(f"  Desviación estándar: {np.std(prom_colas):.2f} minutos")
    print(f"  Mínimo: {np.min(prom_colas):.2f} min, Máximo: {np.max(prom_colas):.2f} min")
    
    print(f"\nTiempo en sistema:")
    print(f"  Promedio de promedios: {np.mean(prom_sistemas):.2f} minutos")
    print(f"  Desviación estándar: {np.std(prom_sistemas):.2f} minutos")
    print(f"  Mínimo: {np.min(prom_sistemas):.2f} min, Máximo: {np.max(prom_sistemas):.2f} min")
    
    print(f"\nOcupación del cajero:")
    print(f"  Promedio: {np.mean(ocupaciones):.2f}%")
    print(f"  Desviación estándar: {np.std(ocupaciones):.2f}%")
    print("=" * 110)
