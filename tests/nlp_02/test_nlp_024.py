#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import util

from nlp_02 import nlp_024

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

https://ja.wikipedia.org/wiki/Help:画像などのファイルのアップロードと利用
"""


def test_execute():
    excepted = util.expected_file(__file__)
    actual = util.list2text(nlp_024.execute("./work/jawiki-country.json.gz"))
    assert excepted == actual
