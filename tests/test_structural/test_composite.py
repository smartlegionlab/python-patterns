# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest

from patterns.structural.composite import Line


class TestComposite:
    def test_add(self, picture, line):
        picture.add(line)
        assert line in picture._children

    def test_remove(self, picture, line):
        picture.add(line)
        assert line in picture._children
        picture.remove(line)
        assert line not in picture._children

    def test_draw(self, picture, line, capfd):
        picture.add(line)
        picture.draw()
        out, _ = capfd.readouterr()
        assert out == 'Line\n'

    def test_get_child(self, picture, line):
        picture.add(line)
        line = picture.get_child(0)
        assert isinstance(line, Line)

    def test_add_err(self, picture):
        with pytest.raises(TypeError):
            picture.add(0)
