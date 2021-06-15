#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_005

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


def test_char_bi_gram():
    arg = "I am an NLPer"
    expected = ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"]
    actual = nlp_005.char_bi_gram(arg)
    print(actual)
    assert expected == actual


def test_word_bi_gram():
    arg = "I am an NLPer"
    expected = [["I", "am"], ["am", "an"], ["an", "NLPer"]]
    actual = nlp_005.word_bi_gram(arg)
    print(actual)
    assert expected == actual
