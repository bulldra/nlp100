#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import util

from nlp_02 import nlp_020

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

https://docs.python.org/ja/3.9/library/gzip.html
"""


def test_execute():
    excepted = util.unix_cmd(f"cat {util.build_expected_path(__file__)}")
    actual = nlp_020.execute("./work/jawiki-country.json.gz")
    assert excepted == actual
