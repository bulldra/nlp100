#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import pandas

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""


def execute(input, num):
    df = pandas.read_csv(
        input, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    return df.tail(num).to_csv(sep="\t", header=None, index=False)
