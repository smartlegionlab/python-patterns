# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestPlaceMark:
    def test_place_mark(self, place_marks):
        pm0, pm1 = place_marks
        assert pm0.color is pm1.color
