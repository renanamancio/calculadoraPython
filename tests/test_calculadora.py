import pytest
from unittest.mock import patch
from tests.calculadora import calcular, entrada_usuario, main

@pytest.mark.parametrize("a, b, op, esperado", [
    (5, 3, "1", 8),
    (-5, -3, "1", -8),
    (5, -3, "1", 2),
    (10, 0, "1", 10),
    (2.5, 2.5, "1", 5.0),
    (5, 3, "2", 2),
    (3, 5, "2", -2),
    (10, 0, "2", 10),
    (-5, -3, "2", -2),
    (5, 3, "3", 15),
    (5, 0, "3", 0),
    (-5, 3, "3", -15),
    (-5, -3, "3", 15),
    (10, 2, "4", 5),
    (9, 2, "4", 4.5),
    (-10, 2, "4", -5),
])

def test_calcular_operacoes_validas(a, b, op, esperado):
    assert calcular(a, b, op) == esperado

def test_calcular_divisao_por_zero():
    resultado = calcular(10, 0, "4")
    assert isinstance(resultado, str)
    assert "Divisão por zero" in resultado

def test_calcular_operacao_invalida():
    assert calcular(10, 5, "5") == "Operação inválida."
    assert calcular(10, 5, "abc") == "Operação inválida."

def test_entrada_usuario_sucesso(monkeypatch):
    entradas_simuladas = ["10", "5", "1"] 
    iterador_entradas = iter(entradas_simuladas)
    monkeypatch.setattr('builtins.input', lambda _: next(iterador_entradas))
    a, b, op = entrada_usuario()
    assert a == 10.0
    assert b == 5.0
    assert op == "1"

def test_entrada_usuario_com_retry(monkeypatch):
    entradas_simuladas = ["abc","20","xyz","10","9","4"]
    iterador_entradas = iter(entradas_simuladas)
    monkeypatch.setattr('builtins.input', lambda _: next(iterador_entradas))

    a, b, op = entrada_usuario()

    assert a == 20.0
    assert b == 10.0
    assert op == "4"

def test_main_execucao_completa(monkeypatch, capsys):
    monkeypatch.setattr('calculadora.entrada_usuario', lambda: (15, 3, "4"))
    main()
    captured = capsys.readouterr()
    assert "O resultado é: 5.0" in captured.out