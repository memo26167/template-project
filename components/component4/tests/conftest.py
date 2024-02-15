"""Docstring of conftest of component4.

This is a file that contains a fixture of a docker container.
"""
from time import sleep
from typing import Generator

import docker  # type: ignore[import-untyped]
import pytest
import redis


# ruff: noqa: T201

# Redis fixture
@pytest.fixture(scope='session')
def _container_fixture() -> Generator[None, None, None]:
    """Implement fixture of a container.

    This is a fixture that creates a container.
    It yields a empty generator and when it ends,
    the container is shutdown.

    Returns
    -------
    `Generator` [`None`, `None`, `None`]
        An empty generator.
    """
    print('This is setup')
    client = docker.from_env()
    container = client.containers.run(
        image='redis',
        auto_remove=True,
        name='test_redis',
        ports={'6379/tcp': ('127.0.0.1', 6379)},
        detach=True,
        remove=True,
        environment={'REDIS_PORT':6379}
    )
    sleep(1)
    while container.status not in ['created', 'running']:
        sleep(1)
        print(container.status)
        continue

    yield

    print('This is teardown')
    container.stop()

@pytest.fixture(scope='session')
def redis_fixture(_container_fixture: Generator[None, None, None]
                  ) -> Generator[redis.Redis, None, None]:
    """Implement fixture of a redis connection.

    This is a fixture that creates a connection to a redis container.
    It yields a generator with the connection and when it ends,
    the connection is shutdown.

    Parameters
    ----------
    _container_fixture : `Generator` [`None`, `None`, `None`]
        An empty generator, but that actually starts a container and
        it's shutdown when the generator is released.

    Returns
    -------
    `Generator` [`redis.Redis`, `None`, `None`]
        A generator that gives a redis connection.
    """
    redis_conn = redis.Redis(port=6379, db=0)
    yield redis_conn
    redis_conn.close()
