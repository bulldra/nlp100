#!/usr/bin/env python3

__version__ = "0.1.0"

import util

from nlp_02 import nlp_026

"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ．

https://ja.wikipedia.org/wiki/Help:早見表
"""


def test_execute():
    excepted = util.expected_file(__file__)
    actual = util.dict2tsv(nlp_026.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
