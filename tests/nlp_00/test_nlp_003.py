#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_00 import nlp_003

"""
03. 円周率
“Now I need a drink, alcoholic of course, after the heavy
lectures involving quantum mechanics.”
という文を単語に分解し，各単語の（アルファベットの）文字数を
先頭から出現順に並べたリストを作成せよ．．
"""


def test_execute():
    arg = "Now I need a drink, alcoholic of course, after the heavy lectures \
involving quantum mechanics."
    excepted = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    actual = nlp_003.execute(arg)
    print(actual)
    assert excepted == actual
