# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestFacade:
    def test_write(self, facade, capfd):
        facade.write('Smart Legion')
        out, err = capfd.readouterr()
        assert out == 'Smart Legion\n'

    def test_write_err(self, facade, capfd):
        facade.write('Smart Legion')
        out, err = capfd.readouterr()
        assert out == 'Error: paper out\n'
