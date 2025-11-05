"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    # TODO: Implementar algoritmo minimax

    # INSTRUCCIONES:
    # 3. La función debe retornar una tupla (fila, columna) con la mejor jugada

    if tateti.jugador(estado) == JUGADOR_MAX:
        sucs = {}

        for accion in tateti.acciones(estado):
            sucs[accion] = MINIMAX_MIN(tateti, tateti.resultado(estado, accion))

        # devuelve la acción con mayor valor
        return max(sucs, key=sucs.get)

    if tateti.jugador(estado) == JUGADOR_MIN:
        sucs = {}

        for accion in tateti.acciones(estado):
            sucs[accion] = MINIMAX_MAX(tateti, tateti.resultado(estado, accion))

        # devuelve la acción con menor valor
        return min(sucs, key=sucs.get)


def MINIMAX_MAX(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    
    valor = float("-inf")

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, MINIMAX_MIN(tateti, sucesor))

    return valor


def MINIMAX_MIN(tateti: Tateti, estado: List[List[str]]) -> float:
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    
    valor = float("inf")

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, MINIMAX_MAX(tateti, sucesor))

    return valor