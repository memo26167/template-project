"""Docstring of conftest of component3.

This is a file that contains fixtures! This means resources that will be
used by test funtions for testing the component3.
"""
# ruff: noqa: T201
from __future__ import annotations

from typing import Generator

from component3.main import Fruit
import pytest


@pytest.fixture()
def my_fruit() -> Fruit:
    """Implement fixture of a fruit.

    Creates a fixture of a Fruit

    Returns
    -------
    `Fruit`
        A fruit, specifically an apple.
    """
    return Fruit('apple')

@pytest.fixture()
def fruit_basket(my_fruit: Fruit) -> list[Fruit]:
    """Implement fixture of a basket of fruits.

    Creates a fixture of a list of Fruit

    Parameters
    ----------
    my_fruit : `Fruit`
        A `Fruit`.

    Returns
    -------
    `list` [`Fruit`]
        A fruit, specifically an apple.
    """
    return [Fruit('banana'), my_fruit]

# Fixture with yield, can be destroyed
@pytest.fixture(scope='session')
def temporal_fruit() -> Fruit:
    """Implement fixture of a temporal fruit.

    Creates a fixture of a Fruit

    Returns
    -------
    `Fruit`
        A fruit, specifically an apple.
    """
    return Fruit('apple')

@pytest.fixture(scope='session')
def temporal_fruit_basket(temporal_fruit: Fruit
                          )-> Generator[list[Fruit], None, None]:
    """Implement fixture of a temporal basket of fruits.

    Creates a fixture of a list of Fruit

    Parameters
    ----------
    temporal_fruit : `Fruit`
        A `Fruit`.

    Returns
    -------
    `Generator` [`Fruit`, `None`, `None`]
        A generator of fruits.

    Notes
    -----
    The return type of generator functions can be annotated
    by the generic typeGenerator[yield_type, send_type, return_type]
    provided by typing.py module
    """
    print('This is setup')
    basket = [Fruit('pineapple'), temporal_fruit]

    print('This is yield')
    print(basket)
    yield basket

    print('This is teardown')
    basket.pop()
    print(basket)
