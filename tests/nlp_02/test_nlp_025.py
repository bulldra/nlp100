#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import util

from nlp_02 import nlp_025

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．

https://ja.wikipedia.org/wiki/Template:基礎情報_国
"""


def test_execute():
    excepted = util.unix_cmd(f"cat {util.build_expected_path(__file__)}")
    actual = util.dict2tsv(nlp_025.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
