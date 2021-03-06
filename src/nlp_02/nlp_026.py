#!/usr/bin/env python3

__version__ = "0.1.0"

import re

from nlp_02 import nlp_025

"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ．

https://ja.wikipedia.org/wiki/Help:早見表
"""


def execute(input):
    return {
        k: re.sub(r"'{2,4}(.+?)'{2,4}", r"\1", v)
        for k, v in nlp_025.execute(input).items()
    }
