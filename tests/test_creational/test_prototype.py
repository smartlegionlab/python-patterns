# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests prototype.py"""
from patterns.creational.prototype import Bird


class TestPrototype:
    def test_register(self, prototype, bird):
        prototype.register('Bird', bird)
        assert 'Bird' in prototype._objects

    def test_unregister(self, prototype, bird):
        prototype.register('Bird', bird)
        prototype.unregister('Bird')
        assert 'Bird' not in prototype._objects

    def test_clone(self, prototype, bird):
        prototype.register('Bird', bird)
        duck = prototype.clone('Bird', {'name': 'Duck'})
        assert isinstance(duck, Bird)

    def test_get_attr(self, prototype, bird):
        prototype.register('Bird', bird)
        duck = prototype.clone('Bird', {'name': 'Duck'})
        assert getattr(duck, 'name')
        assert duck.name == 'Duck'
