# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestRemoteControl:
    def test_channel(self, remote_control):
        assert remote_control._channel == 0

    def test_tune_channel(self, remote_control):
        remote_control.tune_channel(10)
        assert remote_control._channel == 10

    def test_next_channel(self, remote_control):
        remote_control.next_channel()
        assert remote_control._channel == 1

    def test_prev_channel(self, remote_control):
        remote_control.tune_channel(10)
        remote_control.prev_channel()
        assert remote_control._channel == 9
