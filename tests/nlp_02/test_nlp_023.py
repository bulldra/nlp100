#!/usr/bin/env python3

__version__ = "0.1.0"

import util

from nlp_02 import nlp_023

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

https://ja.wikipedia.org/wiki/Help:セクション
"""


def test_execute():
    excepted = util.expected_file(__file__)
    actual = util.matrix2tsv(nlp_023.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
