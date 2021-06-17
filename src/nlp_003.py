#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

"""
03. 円周率
“Now I need a drink, alcoholic of course, after the heavy
lectures involving quantum mechanics.”
という文を単語に分解し，各単語の（アルファベットの）文字数を
先頭から出現順に並べたリストを作成せよ．．
"""


def execute(arg):
    return [len(s) for s in re.sub(r"[^a-zA-Z\s]", "", arg).split(" ")]
