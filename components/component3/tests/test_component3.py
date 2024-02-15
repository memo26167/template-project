"""Docstring of several tests.

This is a module of tests that shows several examples of tests.
"""
# ruff: noqa: T201
from __future__ import annotations

from typing import TYPE_CHECKING

from component3.main import component3_function
import pytest


if TYPE_CHECKING:
    from component3.main import Fruit
    from pytest_benchmark.fixture import (  # type: ignore[import-untyped]
        BenchmarkFixture,
    )



def test_component3() -> None:
    """Test function `component3_function`.

    This is a function that tests the function of the component3.
    """
    result = component3_function('a')
    assert result == 'A'

def test_benchmark_component3(benchmark: BenchmarkFixture) -> None:
    """Test function `component3_function` with benchmark.

    This is a function that tests the function of the component3.

    Parameters
    ----------
    benchmark : BenchmarkFixture
        Fixture Benchmark, extension of Pytest.
    """
    result = benchmark(component3_function, 'a')
    assert result == 'A'

def test_fail_component3() -> None:
    """Test fail of function `component3_function`.

    This is a function that tests the function of the component3
    and expects it to fail.
    """
    with pytest.raises(AttributeError):
        component3_function(1)  # type: ignore[arg-type]

## General tests

# Expected error test
def test_division_by_zero() -> None:
    """Test fail of division by zero.

    This is a function that tests a division by zero
    and expects it to fail.
    """
    with pytest.raises(ZeroDivisionError) as e_info:
        x = 1 / 0  # noqa: F841
    print(e_info)

# Test that is expected to fail but for unfixed bug :(
@pytest.mark.xfail()
def test_xfail() -> None:
    """Test marked to expect fail.

    This is a function that tests an assert
    and expect it to fail. It should be used to mark
    unfixed bugs.
    """
    assert 1 / 0 == 1

# Skipped test
@pytest.mark.skip(reason='why not')
def test_skipped() -> None:
    """Test marked to be skipped.

    This is a function that tests an assert.
    But is marked to be skipped by PyTest.
    """
    assert 1 == 1

# Same test with several inputs and expectations
@pytest.mark.parametrize(('test_input', 'expected'), [
    ('mi noMbre es maTIas', 'MI NOMBRE ES MATIAS'),
    ('hI, ThIs IS johN', 'HI, THIS IS JOHN'),
])
def test_parametrized(test_input: str, expected: str) -> None:
    """Test a function with parametrization.

    This is a function that tests an assert of a returned
    value of a function, with parametrization values.

    Parameters
    ----------
    test_input : str
        An input to be transformed.
    expected : str
        The expected value of the transformation of the input.
    """
    result = component3_function(test_input)
    assert result == expected

# Testing fixture. A fixture is a context in wich a test is executed
# For example, accessing a website, creating a class
# or running a container or a database
def test_my_fruit_in_basket(my_fruit: Fruit, fruit_basket: list[Fruit]) -> None:
    """Test the basket fruit fixture.

    This is a function that tests a fixture, that the Fruit is in a basket.

    Parameters
    ----------
    my_fruit : Fruit
        A single fruit.
    fruit_basket : list[Fruit]
        A basket that should contain the single fruit.
    """
    assert my_fruit in fruit_basket

# Testing fixture that destroys itself
def test_temporal_fruit_in_basket(temporal_fruit: Fruit,
                                  temporal_fruit_basket: list[Fruit]) -> None:
    """Test the temporal basket fruit fixture.

    This is a function that tests a fixture,
    that the temporal Fruit is in the temporal basket.

    Parameters
    ----------
    temporal_fruit : Fruit
        A single fruit.
    temporal_fruit_basket : list[Fruit]
        A basket that should contain the single fruit.
    """
    assert temporal_fruit in temporal_fruit_basket





