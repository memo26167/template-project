"""Docstring of test of component2.

Also a small test example,
but now the component2_function has to use a library.
"""

from component2.main import component2_function
from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import-untyped]


def test_component2() -> None:
    """Test function component2.

    This function tests the behavior of the function component 2.
    """
    result = component2_function(-10)
    assert result == 10

def test_benchmark_component2(benchmark: BenchmarkFixture) -> None:
    """Benchmark function component2.

    This function tests the behavior of the function component 2.

    Parameters
    ----------
    benchmark : BenchmarkFixture
        Fixture Benchmark, extension of Pytest.
    """
    result = benchmark(component2_function, -10)
    assert result == 10
