import pytest
from component4.main import component4_function

def test_component4():
    result = component4_function('a')
    assert result == 'A'

@pytest.mark.slow
@pytest.mark.integration
def test_redis_connection(redis_fixture):
    count = redis_fixture.incrby("a", 1)
    assert count == 1