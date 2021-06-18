#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

from nlp_02 import nlp_020

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

https://ja.wikipedia.org/wiki/Help:カテゴリ
"""


def execute(input):
    text = nlp_020.execute(input)
    return [t for t in text.splitlines() if re.match(r"\[\[Category:.+\]\]", t)]
