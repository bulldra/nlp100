#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

import nlp_020

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

https://ja.wikipedia.org/wiki/Help:セクション
"""


def execute(input):
    text = nlp_020.execute(input)
    sections = [
        re.sub(r"^={2,4}\s*([^\s=]+).*", r"\1", t) + "\t" + str(t.count("=") // 2 - 1)
        for t in text.splitlines()
        if re.match(r"^={2,4}", t)
    ]
    return "\n".join(sections) + "\n"
