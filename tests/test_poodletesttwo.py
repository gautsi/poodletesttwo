#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_poodletesttwo
----------------------------------

Tests for `poodletesttwo` module.
"""

import unittest

from poodletesttwo import poodletesttwo


class TestPoodletesttwo(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert poodletesttwo.test_func() == "hello 2.0 0"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
