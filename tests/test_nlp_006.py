#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nlp_006

'''
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字
bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，
積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''


def test_union():
    expected = {
        'ag', 'ad', 'ra', 'di', 'gr',
        'ap', 'is', 'pa', 'se', 'ph', 'ar'
    }
    actual = nlp_006.union('paraparaparadise', 'paragraph')
    print(actual)
    assert(expected == actual)


def test_intersection():
    expected = {'ap', 'ar', 'pa', 'ra'}
    actual = nlp_006.intersection('paraparaparadise', 'paragraph')
    print(actual)
    assert(expected == actual)


def test_difference():
    expected = {'ad', 'di', 'is', 'se'}
    actual = nlp_006.difference('paraparaparadise', 'paragraph')
    print(actual)
    assert(expected == actual)


def test_find_x():
    expected = True
    actual = nlp_006.find('paraparaparadise', 'se')
    print(actual)
    assert(expected == actual)


def test_find_y():
    expected = False
    actual = nlp_006.find('paragraph', 'se')
    print(actual)
    assert(expected == actual)
