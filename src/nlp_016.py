#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""


def execute(path, tail):
    with open(path, "r") as f1:
        return "\n".join(f1.read().splitlines()[-tail:]) + "\n"
