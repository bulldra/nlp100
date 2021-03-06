#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_01 import nlp_015
import util

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""


def tail(input, num):
    expected = util.unix_cmd(f"tail -n {num} {input}")
    actual = nlp_015.execute(input, num)
    return expected, actual


def test_tail1():
    expected, actual = tail("./work/popular-names.txt", 1)
    assert expected == actual


def test_tail3():
    expected, actual = tail("./work/popular-names.txt", 3)
    assert expected == actual


def test_tail10():
    expected, actual = tail("./work/popular-names.txt", 10)
    assert expected == actual
