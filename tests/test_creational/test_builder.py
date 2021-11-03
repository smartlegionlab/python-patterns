# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests builder.py"""


class TestFlashLight:

    def test_on(self, flashlight):
        flashlight.on()
        assert flashlight._shine
        assert 'On' in str(flashlight)

    def test_off(self, flashlight):
        flashlight.off()
        assert not flashlight._shine
        assert 'Off' in str(flashlight)


class TestFlashLightBuilder:
    def test_build_body(self, flashlight_builder, body):
        assert isinstance(flashlight_builder.build_body(), type(body))

    def test_build_lamp(self, flashlight_builder, lamp):
        assert isinstance(flashlight_builder.build_lamp(), type(lamp))

    def test_build_battery(self, flashlight_builder, battery):
        assert isinstance(flashlight_builder.build_battery(), type(battery))

    def test_create_flashlight(self, flashlight_builder, flashlight):
        assert isinstance(flashlight_builder.create_flashlight(), type(flashlight))
