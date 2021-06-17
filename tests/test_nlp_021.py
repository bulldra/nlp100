#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import nlp_021
import util

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

https://ja.wikipedia.org/wiki/Help:カテゴリ
"""


def test_execute():
    excepted = util.unix_cmd("cat ./tests/test_nlp_021.txt")
    actual = nlp_021.execute("./work/jawiki-country.json.gz")
    assert excepted == actual
