import pytest
from component1.main import component1_function

def test_component1():
    result = component1_function(3)
    assert result == 11

def test_benchmark_component1(benchmark):
    result = benchmark(component1_function, 3)
    assert result == 11
