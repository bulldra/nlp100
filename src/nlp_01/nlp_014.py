#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""


def execute(input, num):
    df = pandas.read_csv(
        input, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    return df.head(num).to_csv(sep="\t", header=None, index=False)
