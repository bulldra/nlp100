#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import nlp_020
import util

"""
20. JSONデータの読み込みPermalink
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

https://docs.python.org/ja/3.9/library/gzip.html
"""


def test_execute():
    excepted = util.unix_cmd("cat ./tests/test_nlp_020.txt")
    actual = nlp_020.execute("./work/jawiki-country.json.gz")
    assert excepted == actual
