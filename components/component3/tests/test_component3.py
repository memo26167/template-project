import pytest
from component3.main import component3_function

def test_component3():
    result = component3_function('a')
    assert result == 'A'

def test_benchmark_component3(benchmark):
    result = benchmark(component3_function, 'a')
    assert result == 'A'

def test_fail_component3():
    with pytest.raises(AttributeError) as e_info:
        result = component3_function(1)

## General tests

# Expected error test 
def test_division_by_zero():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

# Test that is expected to fail but for unfixed bug :(
@pytest.mark.xfail 
def test_xfail():
    assert 1 / 0 == 1

# Skipped test
@pytest.mark.skip(reason="why not")
def test_skipped():
    assert 1 == 1

# Same test with several inputs and expectations
@pytest.mark.parametrize("test_input,expected", [
    ('mi noMbre es guiLLermo', 'MI NOMBRE ES GUILLERMO'),
    ('hI, ThIs IS johN', 'HI, THIS IS JOHN'),
])
def test_parametrized(test_input, expected):
    result = component3_function(test_input)
    assert result == expected

# Testing fixture. A fixture is a context in wich a test is executed
# For example, accessing a website, creating a class
# or running a container or a database
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket

# Testing fixture that destroys itself
def test_temporal_fruit_in_basket(temporal_fruit, temporal_fruit_basket):
    assert temporal_fruit in temporal_fruit_basket





