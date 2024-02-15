"""Docstring of test of component1.

Just a small test example.
"""

from component1.main import component1_function
from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import-untyped]


def test_component1() -> None:
    """Test function component1.

    This function tests the behavior of the function component 1.
    """
    result = component1_function(3)
    assert result == 11

def test_benchmark_component1(benchmark: BenchmarkFixture) -> None:
    """Benchmark function component1.

    This function tests the behavior of the function component 1.

    Parameters
    ----------
    benchmark : BenchmarkFixture
        Fixture Benchmark, extension of Pytest.
    """
    result = benchmark(component1_function, 3)
    assert result == 11
