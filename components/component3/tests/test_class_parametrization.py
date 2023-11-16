import pytest

@pytest.mark.parametrize(
    ("param1", "param2"),
    [("a", "b"),
     ("c", "d")]
)
class TestGroup:
    """A class with common parameters, `param1` and `param2`."""

    @pytest.fixture
    def fixt(self) -> int:
        """This fixture will only be available within the scope of TestGroup"""
        return 123

    def test_one(self, param1: str, param2: str, fixt: int) -> None:
        print("\ntest_one", param1, param2, fixt)

    def test_two(self, param1: str, param2: str) -> None:
        print("\ntest_two", param1, param2)