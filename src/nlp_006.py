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


def union(arg1, arg2):
    x = nlp_005.char_bi_gram(arg1)
    y = nlp_005.char_bi_gram(arg2)
    return set(x).union(set(y))


def intersection(arg1, arg2):
    x = nlp_005.char_bi_gram(arg1)
    y = nlp_005.char_bi_gram(arg2)
    return set(x) & set(y)


def difference(arg1, arg2):
    x = nlp_005.char_bi_gram(arg1)
    y = nlp_005.char_bi_gram(arg2)
    return set(x) - set(y)


def find(arg1, t):
    return t in nlp_005.char_bi_gram(arg1)
