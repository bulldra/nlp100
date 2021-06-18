#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_00 import nlp_006

"""
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字
bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，
積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

arg1 = "paraparaparadise"
arg2 = "paragraph"


def test_union():
    expected = {"ag", "ad", "ra", "di", "gr", "ap", "is", "pa", "se", "ph", "ar"}
    actual = nlp_006.union(arg1, arg2)
    print(actual)
    assert expected == actual


def test_intersection():
    expected = {"ap", "ar", "pa", "ra"}
    actual = nlp_006.intersection(arg1, arg2)
    print(actual)
    assert expected == actual


def test_difference():
    expected = {"ad", "di", "is", "se"}
    actual = nlp_006.difference(arg1, arg2)
    print(actual)
    assert expected == actual


def test_find_x():
    expected = True
    actual = nlp_006.find(arg1, "se")
    print(actual)
    assert expected == actual


def test_find_y():
    expected = False
    actual = nlp_006.find(arg2, "se")
    print(actual)
    assert expected == actual
