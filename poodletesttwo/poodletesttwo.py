# -*- coding: utf-8 -*-
import numpy as np


def test_func():
    """
    A test function for doctests and unitests with tox. This is
    second testing and stuff.
    For example,

    >>> test_func()
    'hello 2.0'

    >>> 1 + 2
    3

    >>> np.sqrt(4)
    2.0

    """
    return "hello {}".format(np.sqrt(4))
