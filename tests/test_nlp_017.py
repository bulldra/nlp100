#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import nlp_017
import util

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
"""


def test_word_uniq():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"cut -f 1 {input} | sort | uniq")
    actual = nlp_017.execute(input)
    assert actual == expected
