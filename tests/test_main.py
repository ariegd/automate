#!/usr/bin/python3
# tests/test_main.py

from main import sumar, restar

def test_sumar_numeros_positivos():
    """
    Prueba que la función sumar funciona con números positivos.
    """
    assert sumar(2, 3) == 5
    
    if(sumar(2, 3) == 5):
        print("Prueba que la función sumar funciona con números positivos.")
    else:
        print("False")

def test_sumar_numeros_negativos():
    """
    Prueba que la función sumar funciona con números negativos.
    """
    assert sumar(-1, -1) == -2

def test_restar():
    """
    Prueba que la función restar funciona correctamente.
    """
    assert restar(5, 2) == 3
    assert restar(10, 5) == 5

def test_restar_resultado_negativo():
    """
    Prueba que la función restar funciona con resultados negativos.
    """
    assert restar(2, 5) == -3
    
# Test
test_sumar_numeros_positivos()
test_sumar_numeros_negativos()
test_restar()
test_restar_resultado_negativo()
