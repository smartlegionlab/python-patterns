# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest

from patterns.structural.adapter import Dog, CatAdapter
from patterns.structural.bridge import RemoteControl
from patterns.structural.composite import Picture, Rectangle, Text, Line
from patterns.structural.decorator import Man, JetPack
from patterns.structural.facade import Facade, Paper, Printer


# Adapter ---------------------------------------------------
from patterns.structural.flyweight import PlaceMark
from patterns.structural.proxy import Image, ImageProxy


@pytest.fixture(name="dog")
def get_dog():
    return Dog('Brave')


@pytest.fixture(name='cat_adapter')
def get_cat_adapter():
    return CatAdapter


# Bridge ----------------------------------------------------

@pytest.fixture(name='remote_control')
def get_remote_control():
    return RemoteControl()


# Composite -------------------------------------------------

@pytest.fixture(name='picture')
def get_picture():
    return Picture()


@pytest.fixture(name='line')
def get_line():
    return Line()


@pytest.fixture(name='rectangle')
def get_rectangle():
    return Rectangle()


@pytest.fixture(name='text')
def get_text():
    return Text()


# Decorator ------------------------------------------------

@pytest.fixture(scope='class', name='man')
def get_man():
    return Man('Smart Bear')


@pytest.fixture(scope="class", name="man_jet")
def get_man_jet(man):
    man_jat = JetPack(man)
    return man_jat


# Facade ---------------------------------------------------

@pytest.fixture(scope="class", name="paper")
def get_paper():
    return Paper(1)


@pytest.fixture(scope="class", name="printer")
def get_printer():
    return Printer()


@pytest.fixture(scope="class", name="facade")
def get_facade():
    return Facade()


# Flyweight ------------------------------------------------

@pytest.fixture(scope="session", name='place_marks')
def place_marks():
    place_mark0 = PlaceMark(-74.007121, 40.714551, 'green')
    place_mark1 = PlaceMark(37.987654, 89.433265, 'green')
    return place_mark0, place_mark1


# Flyweight ------------------------------------------------

@pytest.fixture(name='image')
def get_image():
    return Image(200, 200)


@pytest.fixture(name='image_proxy')
def get_image_proxy():
    return ImageProxy(200, 200)
