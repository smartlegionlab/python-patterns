# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests singleton.py"""


def test_singleton(singletons):
    sing1, sing2 = singletons
    assert sing1 == sing2
