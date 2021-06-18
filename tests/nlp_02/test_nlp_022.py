#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import util

from nlp_02 import nlp_022

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""


def test_execute():
    excepted = util.expected_file(__file__)
    actual = util.list2text(nlp_022.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
