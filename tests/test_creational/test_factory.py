# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests factory.py"""
import pytest

from patterns.creational.factory import PDFDocument, ODFDocument, NoneDocument


class TestApplication:
    @pytest.mark.parametrize('type_, obj', [('pdf', PDFDocument),
                                            ('odf', ODFDocument),
                                            ('bad', NoneDocument)])
    def test_create_doc(self, obj, app, type_):
        assert isinstance(app.create_doc(type_), obj)
