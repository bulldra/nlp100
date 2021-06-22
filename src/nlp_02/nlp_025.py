#!/usr/bin/env python3

__version__ = "0.1.0"

import re

from nlp_02 import nlp_020

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．

https://ja.wikipedia.org/wiki/Template:基礎情報_国
"""


def execute(input):
    template_block = re.findall(
        r"\{\{基礎情報.*?\n(.+?)^\}\}$",
        nlp_020.execute(input),
        flags=re.DOTALL + re.MULTILINE,
    )[0]
    template_elems = re.findall(
        r"\|(.+?)\s*=\s*(.+?)(?=\n\||(?=\n$))",
        template_block,
        flags=re.DOTALL + re.MULTILINE,
    )
    return {x[0]: x[1] for x in template_elems}
