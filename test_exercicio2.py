from exercicio2 import calcular_frete

def test_frete_peso_zero_deve_retornar_zero():
    assert calcular_frete(0) == 0.0

def test_frete_peso_negativo_deve_retornar_zero():
    assert calcular_frete(-10) == 0.0

def test_frete_ate_1kg_deve_retornar_5():
    assert calcular_frete(1.0) == 5.0

def test_frete_acima_1kg_ate_5kg_deve_retornar_10():
    assert calcular_frete(1.01) == 10.0
    assert calcular_frete(3.0) == 10.0
    assert calcular_frete(5.0) == 10.0

def test_frete_acima_5kg_deve_retornar_18():
    assert calcular_frete(5.01) == 18.0
    assert calcular_frete(20.0) == 18.0
