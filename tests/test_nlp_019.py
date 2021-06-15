#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_019
import util

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""


def test_word_freq():
    input = "./work/popular-names.txt"
    cmd = f"cut -f 1 {input} | sort | uniq  -c | sort -k 1nr -k 2 | sed -e 's/^ *[0-9]* //'"
    expected = util.unix_cmd(cmd)
    actual = nlp_019.execute(input)
    assert expected == actual
