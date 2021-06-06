#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_005

'''
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字
bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，
積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''


def __set(arg1, arg2):
    x = set(nlp_005.char_bi_gram(arg1))
    y = set(nlp_005.char_bi_gram(arg2))
    return x, y


def union(arg1, arg2):
    x, y = __set(arg1, arg2)
    return x.union(y)


def intersection(arg1, arg2):
    x, y = __set(arg1, arg2)
    return x & y


def difference(arg1, arg2):
    x, y = __set(arg1, arg2)
    return x - y


def find(arg1, t):
    return t in nlp_005.char_bi_gram(arg1)