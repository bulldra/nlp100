#!/usr/bin/env python3

__version__ = "0.1.0"

import util

from nlp_02 import nlp_027

"""
27. 内部リンクの除去Permalink
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ．

https://ja.wikipedia.org/wiki/Help:早見表
"""


def test_execute():
    excepted = util.expected_file(__file__)
    actual = util.dict2tsv(nlp_027.execute("./work/jawiki-country.json.gz"))


#    assert excepted == actual
