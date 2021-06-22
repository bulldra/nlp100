#!/usr/bin/env python3

__version__ = "0.1.0"

import util

from nlp_01 import nlp_011

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""


def test_sed():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"sed -e 's/\t/ /g' {input}")
    actual = nlp_011.execute(input)
    assert expected == actual


def test_tr():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"cat {input} | tr '\t' ' '")
    actual = nlp_011.execute(input)
    assert expected == actual


def test_expand():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"expand -t 1 {input}")
    actual = nlp_011.execute(input)
    assert expected == actual
