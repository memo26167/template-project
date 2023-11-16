import pytest

# Fruits fixture
class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

# Fixture with yield, can be destroyed
@pytest.fixture(scope="session")
def temporal_fruit():
    yield Fruit("apple")

@pytest.fixture(scope="session")
def temporal_fruit_basket(temporal_fruit):
    '''
    To see the prints, you must run pytest with -s flag
    '''
    print("This is setup")
    basket = [Fruit("pineapple"), temporal_fruit]

    print("This is yield")
    print(basket)
    yield basket

    print("This is teardown")
    basket.pop()
    print(basket)
