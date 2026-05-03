"""
Ejercicio 1: Cafetería Universitaria
Duración: 4 horas (240 minutos)
Llegadas: Exponencial(media=3 minutos)
Servicio: Uniforme[2, 4] minutos
Recurso: 1 cajero
"""

import simpy
import numpy as np

def cliente(env, name, cajero, rng, registros):
    """
    Simula el proceso de un cliente en la cafetería.
    
    Args:
        env: Entorno de SimPy
        name: Nombre del cliente
        cajero: Recurso compartido (servidor)
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    llegada = env.now
    
    # Solicitar el cajero
    with cajero.request() as req:
        yield req
        tiempo_espera = env.now - llegada
        registros['tiempos_cola'].append(tiempo_espera)
        
        # Registrar cola máxima en el momento de ser atendido
        cola_actual = len(cajero.queue)
        if cola_actual > registros['max_cola']:
            registros['max_cola'] = cola_actual
        
        # Servicio uniforme [2, 4] minutos
        tiempo_servicio = rng.uniform(2, 4)
        registros['tiempo_uso_cajero'] += tiempo_servicio
        yield env.timeout(tiempo_servicio)
        
        # Tiempo total en el sistema
        tiempo_sistema = env.now - llegada
        registros['tiempos_sistema'].append(tiempo_sistema)


def llegadas(env, cajero, rng, registros):
    """
    Genera llegadas de clientes con distribución exponencial.
    
    Args:
        env: Entorno de SimPy
        cajero: Recurso compartido
        rng: Generador de números aleatorios
        registros: Diccionario para almacenar métricas
    """
    i = 0
    while env.now < 240:  # Límite de 4 horas
        tiempo_llegada = rng.exponential(3)  # Media 3 minutos
        yield env.timeout(tiempo_llegada)
        if env.now < 240:  # Solo crear cliente si no ha pasado el cierre
            i += 1
            env.process(cliente(env, f'Estudiante {i}', cajero, rng, registros))


def ejecutar_simulacion_e1(semilla):
    """
    Ejecuta una corrida de simulación de la cafetería.
    
    Args:
        semilla: Semilla para reproducibilidad
        
    Returns:
        Tupla con: (atendidos, prom_cola, prom_sistema, ocupacion, max_cola)
    """
    env = simpy.Environment()
    rng = np.random.default_rng(semilla)
    cajero = simpy.Resource(env, capacity=1)
    
    registros = {
        'tiempos_cola': [],
        'tiempos_sistema': [],
        'tiempo_uso_cajero': 0,
        'max_cola': 0
    }
    
    env.process(llegadas(env, cajero, rng, registros))
    env.run(until=240)
    
    total_atendidos = len(registros['tiempos_sistema'])
    promedio_cola = np.mean(registros['tiempos_cola']) if total_atendidos > 0 else 0
    promedio_sistema = np.mean(registros['tiempos_sistema']) if total_atendidos > 0 else 0
    ocupacion = (registros['tiempo_uso_cajero'] / 240) * 100
    
    return total_atendidos, promedio_cola, promedio_sistema, ocupacion, registros['max_cola']


if __name__ == "__main__":
    print("=" * 80)
    print("EJERCICIO 1: CAFETERÍA UNIVERSITARIA")
    print("=" * 80)
    print(f"{'Semilla':<8} {'Atendidos':<12} {'Prom. Cola (min)':<20} {'Prom. Sistema (min)':<20} {'Ocupación (%)':<15} {'Max Cola':<10}")
    print("-" * 80)
    
    resultados = []
    for semilla in [1, 2, 3]:
        res = ejecutar_simulacion_e1(semilla)
        resultados.append(res)
        print(f"{semilla:<8} {res[0]:<12} {res[1]:<20.2f} {res[2]:<20.2f} {res[3]:<15.2f} {res[4]:<10}")
    
    # Estadísticas agregadas
    print("-" * 80)
    atendidos = np.array([r[0] for r in resultados])
    prom_colas = np.array([r[1] for r in resultados])
    prom_sist = np.array([r[2] for r in resultados])
    ocupaciones = np.array([r[3] for r in resultados])
    
    print(f"\n{'AGREGADOS PARA LAS 3 CORRIDAS':<50}")
    print(f"Clientes atendidos - Promedio: {np.mean(atendidos):.1f}, Desv. Est.: {np.std(atendidos):.1f}")
    print(f"Tiempo en cola - Promedio: {np.mean(prom_colas):.2f} min, Desv. Est.: {np.std(prom_colas):.2f}")
    print(f"Tiempo en sistema - Promedio: {np.mean(prom_sist):.2f} min, Desv. Est.: {np.std(prom_sist):.2f}")
    print(f"Ocupación cajero - Promedio: {np.mean(ocupaciones):.2f}%, Desv. Est.: {np.std(ocupaciones):.2f}%")
    print("=" * 80)
