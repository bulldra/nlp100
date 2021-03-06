#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_01 import nlp_014
import util

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""


def head(input, num):
    expected = util.unix_cmd(f"head -n {num} {input}")
    actual = nlp_014.execute(input, num)
    return expected, actual


def test_head1():
    expected, actual = head("./work/popular-names.txt", 1)
    assert expected == actual


def test_head3():
    expected, actual = head("./work/popular-names.txt", 3)
    assert expected == actual


def test_head10():
    expected, actual = head("./work/popular-names.txt", 10)
    assert expected == actual
