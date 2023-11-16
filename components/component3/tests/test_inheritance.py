import pytest

class TestClass:
    VAR: int = 3
    DATA: int = 4

    def test_var_positive(self) -> None:
        assert self.VAR >= 0


class TestSubclass(TestClass):
    VAR: int = 8

    def test_var_even(self) -> None:
        assert self.VAR % 2 == 0

    def test_data(self) -> None:
        assert self.DATA == 4