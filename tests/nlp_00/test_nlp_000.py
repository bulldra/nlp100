#!/usr/bin/env python3

__version__ = "0.1.0"

from nlp_00 import nlp_000

"""
00. 文字列の逆順
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""


def test_execute():
    arg = "stressed"
    excepted = "desserts"
    actual = nlp_000.execute(arg)
    print(actual)
    assert excepted == actual
