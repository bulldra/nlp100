#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

import nlp_020

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""


def execute(input):
    text = nlp_020.execute(input)
    categories = [
        re.sub(r"\[\[Category:([^\|\s]+).*\]\]", r"\1", t)
        for t in text.splitlines()
        if re.match(r"\[\[Category:.+\]\]", t)
    ]
    return "\n".join(categories) + "\n"
