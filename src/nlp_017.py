#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
"""

import pandas


def execute(path):
    df = pandas.read_csv(
        path, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    return "\n".join(df.sort_values("name")["name"].unique()) + "\n"
