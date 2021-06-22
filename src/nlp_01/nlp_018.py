#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""


def execute(path):
    df = pandas.read_csv(
        path, sep="\t", header=None, names=["name", "gender", "num", "year"]
    )
    df = df.sort_values(["num", "name"], ascending=[False, True]).reset_index(drop=True)
    return df.to_csv(sep="\t", index=False, header=None)
