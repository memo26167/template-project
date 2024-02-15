"""Docstring of component3.

A longer description.
"""


def component3_function(x: str) -> str:
    """Implement function component3.

    A description of the function component3.

    Parameters
    ----------
    x : `str`
        Description of parameter `x`.

    Returns
    -------
    `str`
        Description of the return value.

    Notes
    -----
    This is the third component function that will be evaluated.
    """
    return x.upper()

class Fruit:
    """Class that defines a fruit.

    Just a class that defines a fruit.

    Attributes
    ----------
    name : `str`
        The name of the fruit.

    Methods
    -------
    __eq__
        Checks if two fruits are equal.
    __repr__
        Gives a representation of the fruit.

    """

    def __init__(self, name: str):
        """Initialize the Fruit.

        This method initializes the Fruit.

        Parameters
        ----------
        name : `str`
            Another `str`.
        """
        self.name = name

    def __eq__(self, other: object):
        """Compare two fruits.

        This method compare two fruits.

        Parameters
        ----------
        other : `Fruit`
            Another `Fruit`.

        Returns
        -------
        `bool`
            Whether the two fruits are equal or not.
        """
        if not isinstance(other, Fruit):
            return NotImplemented
        return self.name == other.name

    def __repr__(self):
        """Represent the fruit.

        This method creates a representation for the fruit.

        Returns
        -------
        `str`
            The name of the fruit.
        """
        return self.name

if __name__ == '__main__':
    pass
