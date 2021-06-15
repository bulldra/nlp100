#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_014
import util

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""


def test_head1():
    arg1 = 1
    arg2 = "./work/popular-names.txt"
    expected = util.unix_cmd(f"head -n {arg1} {arg2}")
    actual = nlp_014.execute(arg2, arg1)
    assert expected == actual


def test_head3():
    arg1 = 3
    arg2 = "./work/popular-names.txt"
    expected = util.unix_cmd(f"head -n {arg1} {arg2}")
    actual = nlp_014.execute(arg2, arg1)
    assert expected == actual


def test_head10():
    arg1 = 10
    arg2 = "./work/popular-names.txt"
    expected = util.unix_cmd(f"head -n {arg1} {arg2}")
    actual = nlp_014.execute(arg2, arg1)
    assert expected == actual
