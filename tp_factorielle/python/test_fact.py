# python/test_fact.py - À compléter
import math
import pytest
from fact import fact

def test_base():
    # TODO-1: cas simples (0, 1, 5)
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120

def test_against_math():
    # TODO-2: comparer fact(n) à math.factorial(n) pour n in [0..100]
    for n in range(101):
        assert fact(n) == math.factorial(n)

def test_errors():
    # TODO-3: fact(-1) -> ValueError
    with pytest.raises(ValueError):
        fact(-1)
    
    # TODO-4: fact(3.14) -> TypeError
    with pytest.raises(TypeError):
        fact(3.14)