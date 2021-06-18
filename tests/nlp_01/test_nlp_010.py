#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import util

from nlp_01 import nlp_010

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""


def test_execute():
    input = "./work/popular-names.txt"
    expected = util.unix_cmd(f"cat {input} | wc -l").rstrip()
    actual = str(nlp_010.execute(input))
    assert expected == actual
