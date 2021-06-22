#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""


def execute(path):
    df = pandas.read_csv(
        path, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    df = df.groupby("name").size().reset_index(name="freq")
    df = df.sort_values(["freq", "name"], ascending=[False, True])
    return df[["name"]].to_csv(sep="\t", index=False, header=None)
