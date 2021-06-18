#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import re

from nlp_02 import nlp_020

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

https://ja.wikipedia.org/wiki/Help:画像などのファイルのアップロードと利用
"""


def execute(input):
    text = nlp_020.execute(input)
    files = [x for x in re.findall(r"\[\[ファイル:\s*([^]\|]+?)\|", text)]
    return "\n".join(files) + "\n"
