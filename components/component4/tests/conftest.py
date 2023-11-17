import pytest
import docker # type: ignore
import redis
from time import sleep

# Redis fixture
@pytest.fixture(scope="session")
def container_fixture():
    '''
    This fixture starts redis container
    '''
    print("This is setup")
    #client = docker.DockerClient("unix:///home/memo/.docker/desktop/docker.sock")
    client = docker.from_env()
    container = client.containers.run(
        image="redis",
        auto_remove=True,
        name="test_redis",
        ports={"6379/tcp": ("127.0.0.1", 6379)},
        detach=True,
        remove=True,
        environment={"REDIS_PORT":6379}
    )
    sleep(1)
    while not (container.status in ['created', 'running']):
        sleep(1)
        print(container.status)
        continue

    yield 

    print("This is teardown")
    container.stop()

@pytest.fixture(scope="session")
def redis_fixture(container_fixture):
    redis_conn = redis.Redis(port=6379, db=0)
    yield redis_conn
    redis_conn.close()