"""Docstring of test of class parametrization.

This is a module of a test that shows an example of a test
with class parametrization.
This is a file that contains fixtures! This means resources that will be
used by test funtions for testing the component3.
"""
# ruff: noqa: T201
import pytest


@pytest.mark.parametrize(
    ('param1', 'param2'),
    [('a', 'b'),
     ('c', 'd')]
)
class TestGroup:
    """A class with common parameters, `param1` and `param2`."""

    @pytest.fixture()
    def fixt(self) -> int:
        """Implement a fixture.

        This fixture will only be available within the scope of TestGroup.

        Returns
        -------
        `int`
            An integer number.
        """
        return 123

    def test_one(self, param1: str, param2: str, fixt: int) -> None:
        """Test the return value of a function.

        This functions test the return value of a function.
        """
        print('\ntest_one', param1, param2, fixt)

    def test_two(self, param1: str, param2: str) -> None:
        """Test the return value of a function.

        This functions test the return value of a function.
        """
        print('\ntest_two', param1, param2)
