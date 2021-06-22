#!/usr/bin/env python3

__version__ = "0.1.0"

import re

from nlp_02 import nlp_020

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

https://ja.wikipedia.org/wiki/Help:セクション
"""


def execute(input):
    text = nlp_020.execute(input)
    return [
        [x[1], len(x[0]) - 1]
        for x in re.findall(r"(={2,4})\s*([^\|]+?)\s*={2,4}", text)
    ]
