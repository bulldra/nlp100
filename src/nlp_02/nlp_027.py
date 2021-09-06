#!/usr/bin/env python3

__version__ = "0.1.0"

import re

from nlp_02 import nlp_026

"""
27. 内部リンクの除去Permalink
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ．

https://ja.wikipedia.org/wiki/Help:早見表
"""


def execute(input):
    pipe = {
        k: re.sub(r"\[\[(?!ファイル:)(.+?)\|(.+?)\]\]", r"\2", v)
        for k, v in nlp_026.execute(input).items()
    }
    return {k: re.sub(r"\[\[(?!ファイル:)(.+?)\]\]", r"\1", v) for k, v in pipe.items()}
