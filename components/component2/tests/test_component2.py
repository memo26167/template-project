import pytest
from component2.main import component2_function

def test_component2():
    result = component2_function(-10)
    assert result == 10

def test_benchmark_component2(benchmark):
    result = benchmark(component2_function, -10)
    assert result == 10
