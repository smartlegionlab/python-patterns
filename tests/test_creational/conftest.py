# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest

from patterns.creational.abstract_factory import (Drink, Food, ConcreteFactory1,
                                                  ConcreteFactory2, get_factory)
from patterns.creational.builder import Body, Battery, Lamp, FlashLight, FlashLightBuilder
from patterns.creational.factory import Application, NoneDocument, ODFDocument, PDFDocument
from patterns.creational.prototype import Prototype, Bird
from patterns.creational.singleton import Singleton


@pytest.fixture(name='drink')
def get_drink():
    return Drink


@pytest.fixture(name='food')
def get_food():
    return Food


@pytest.fixture(name='fac1')
def get_fac1():
    return ConcreteFactory1()


@pytest.fixture(name='fac2')
def get_fac2():
    return ConcreteFactory2()


@pytest.fixture(name='get_factory')
def fix_get_factory():
    return get_factory


@pytest.fixture(name='drink_obj')
def get_drink_obj():
    return Drink('Coca Cola')


@pytest.fixture(name='food_obj')
def get_food_obj():
    return Food('Nuts')


@pytest.fixture(scope='session', name='body')
def get_body():
    return Body()


@pytest.fixture(scope='session', name='battery')
def get_battery():
    return Battery()


@pytest.fixture(scope='session', name='lamp')
def get_lamp():
    return Lamp()


@pytest.fixture(scope='session', name='flashlight')
def get_flashlight(body, battery, lamp):
    return FlashLight(body=body, lamp=lamp, battery=battery)


@pytest.fixture(scope='session', name='flashlight_builder')
def get_flashlight_builder():
    return FlashLightBuilder()


@pytest.fixture(name='pdf_doc')
def get_pdf():
    return PDFDocument()


@pytest.fixture(name='odf_doc')
def get_odf():
    return ODFDocument()


@pytest.fixture(name='none_doc')
def get_none():
    return NoneDocument()


@pytest.fixture(name='app')
def get_app():
    return Application()


@pytest.fixture(scope='session', name='prototype')
def get_prototype():
    return Prototype()


@pytest.fixture(scope='function', name='bird')
def get_bird():
    return Bird()


@pytest.fixture(scope='session', name='singletons')
def get_singleton():
    return Singleton(), Singleton()
