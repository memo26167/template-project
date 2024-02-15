"""Testing of redis container.

This is a module of a test shows an example of how to test a container.
"""
from component4.main import component4_function
import pytest
import redis


def test_component4() -> None:
    """Test function `component4_function`.

    This is a function that tests the function of the component4.
    """
    result = component4_function('a')
    assert result == 'A'

@pytest.mark.slow()
@pytest.mark.integration()
def test_redis_connection(redis_fixture: redis.Redis) -> None:
    """Test a redis connection.

    This is a function that tests a redis connection to a redis container.

    Parameters
    ----------
    redis_fixture : redis.Redis
        A redis conection that can be used
        to give instructions to a redis container.
    """
    count = redis_fixture.incrby('a', 1)
    assert count == 1
