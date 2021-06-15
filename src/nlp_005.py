#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(arg, n):
    return [arg[i : i + n] for i in range(len(arg) - n + 1)]


def char_bi_gram(arg):
    return n_gram(arg, 2)


def word_bi_gram(arg):
    return n_gram(arg.split(" "), 2)
