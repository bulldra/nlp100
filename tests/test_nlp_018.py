#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_018
import util

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""


def test_word_sort():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"sort -k 3nr -k 1 {input}")
    actual = nlp_018.execute(input)
    assert actual == expected
