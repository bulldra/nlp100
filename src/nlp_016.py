#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""


def execute(input, number, out):
    with open(input, "r") as f:
        text = f.read().splitlines()
        flagsize = len(text) // number + 1
        for n in range(number):
            with open(f"{out}{n:02d}", "w") as w:
                start = n * flagsize
                end = min((n + 1) * flagsize, len(text))
                w.write("\n".join(text[start:end]) + "\n")
