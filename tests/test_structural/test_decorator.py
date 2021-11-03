# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestDecorator:
    def test_fly(self, man_jet, capfd):
        man_jet.fly()
        out, err = capfd.readouterr()
        assert out == 'Smart Bear flies on a jetpack.\n'


def test_man(man, capfd):
    man.say()
    out, err = capfd.readouterr()
    assert out == 'Hello, my name is Smart Bear.\n'
