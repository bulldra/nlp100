#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_016
import util

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""


def test_split1():
    arg1 = 1
    arg2 = "./work/popular-names.txt"
    util.unix_cmd(f"split -l {arg1} {arg2} ./work/split_expected1_")


#    actual = nlp_016.execute(arg2, arg1, "./work/split_actual3_")
#    assert expected == actual

"""
def test_split3():
    arg1 = 3
    arg2 = "./work/popular-names.txt"
    expected = util.unix_cmd(f"split -l {arg1} {arg2} ./work/split_expected3_")
    actual = nlp_016.execute(arg1, arg2, "./work/split_actual3_")
    assert expected == actual
"""
