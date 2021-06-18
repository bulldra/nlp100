#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from nlp_01 import nlp_013
import util

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""


def test_execute():
    arg1 = "./work/col1.txt"
    arg2 = "./work/col2.txt"
    expected = util.unix_cmd(f"paste {arg1} {arg2}")
    actual = nlp_013.execute(arg1, arg2)
    assert expected == actual
