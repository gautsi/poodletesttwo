# -*- coding: utf-8 -*-
"""A test package for things."""
import numpy as np
import pandas as pd
import praw as pr
import time as tm
from sqlalchemy.exc import StatementError


def test_func():
    """
    A test function for doctests and unitests with tox.

    This is second testing and stuff.
    For example,

    >>> a = test_func()
    >>> a
    'hello 2.0 0'

    >>> 1 + 2
    3

    >>> np.sqrt(4)
    2.0

    """
    df = pd.DataFrame([0])
    red = pr.Reddit(user_agent='creddit_score')
    del red
    a = tm.time()
    del a
    return "hello {} {}".format(np.sqrt(4), df[0][0])
