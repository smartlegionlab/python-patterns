# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from patterns.structural.adapter import Dog


class TestDog:
    def test_dog(self, dog):
        assert isinstance(dog, Dog)

    def test_bark(self, dog):
        assert dog.bark() == 'Brave: wof! wof!'


class TestAdapter:
    def test_cat_adapter(self, dog, cat_adapter):
        dog = cat_adapter('Brave')
        assert dog.bark() == 'Brave: meow! meow!'
