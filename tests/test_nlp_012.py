#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_012
import util

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""


def test_col1():
    arg1 = 1
    arg2 = "./work/popular-names.txt"
    arg3 = "./work/col1.txt"
    expected = util.unix_cmd(f"cut -f {arg1} {arg2}")
    nlp_012.out(arg1, arg2, arg3)
    actual = util.unix_cmd(f"cat {arg3}")
    assert expected == actual


def test_col2():
    arg1 = 2
    arg2 = "./work/popular-names.txt"
    arg3 = "./work/col2.txt"
    expected = util.unix_cmd(f"cut -f {arg1} {arg2}")
    nlp_012.out(arg1, arg2, arg3)
    actual = util.unix_cmd(f"cat {arg3}")
    assert expected == actual
