#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
"""


def execute(input):
    df = pandas.read_csv(
        input, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    return "\n".join(df["name"].sort_values().unique()) + "\n"
