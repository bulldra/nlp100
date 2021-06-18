#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import util

from nlp_02 import nlp_021

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

https://ja.wikipedia.org/wiki/Help:カテゴリ
"""


def test_execute():
    excepted = util.unix_cmd(f"cat {util.build_expected_path(__file__)}")
    actual = util.list2text(nlp_021.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
