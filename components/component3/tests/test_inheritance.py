"""Docstring of module of test of inheritance.

This is a module of a test that tests inheritance of classes.
"""

class TestClass:
    """A simple class with a test.

    A class that have two attributes and a test method.

    Attributes
    ----------
    VAR : int
        A attribute VAR
    DATA : int
        A attribute DATA

    Methods
    -------
    test_var_positive()
        A method that test that the VAR attribute is positive.
    """

    VAR: int = 3
    DATA: int = 4

    def test_var_positive(self) -> None:
        """Test that the VAR attribute is positive.

        A method that test that the VAR attribute is positive.
        """
        assert self.VAR >= 0


class TestSubclass(TestClass):
    """A class that inherit attributes from another class.

    A class that inherit attributes from another class
    and define an attribute.

    Attributes
    ----------
    VAR : int
        A attribute VAR

    Methods
    -------
    test_var_even()
        A method that test that the VAR attribute is even.
    test_data()
        A method that test that the DATA attribute is 4.
    """

    VAR: int = 8

    def test_var_even(self) -> None:
        """Test that the VAR attribute is even.

        A method that test that the VAR attribute is even.
        """
        assert self.VAR % 2 == 0

    def test_data(self) -> None:
        """Test that the DATA attribute is 4.

        A method that test that the DATA attribute is 4.
        """
        assert self.DATA == 4
