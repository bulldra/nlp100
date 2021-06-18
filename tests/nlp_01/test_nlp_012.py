#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_01 import nlp_012
import util

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""


def cut(col, input, output):
    expected = util.unix_cmd(f"cut -f {col} {input}")
    nlp_012.execute(col, input, output)
    actual = util.unix_cmd(f"cat {output}")
    return expected, actual


def test_col1():
    col = 1
    input = "./work/popular-names.txt"
    output = "./work/col1.txt"
    expected, actual = cut(col, input, output)
    assert expected == actual


def test_col2():
    col = 2
    input = "./work/popular-names.txt"
    output = "./work/col2.txt"
    expected, actual = cut(col, input, output)
    assert expected == actual
