#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import nlp_023
import util

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

https://ja.wikipedia.org/wiki/Help:セクション
"""


def test_execute():
    excepted = util.unix_cmd("cat ./tests/test_nlp_023.txt")
    actual = nlp_023.execute("./work/jawiki-country.json.gz")

    with open("./work/test_nlp_023.txt", "w") as f:
        f.write(actual)

    assert excepted == actual
