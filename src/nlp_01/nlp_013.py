#!/usr/bin/env python3

__version__ = "0.1.0"

import pandas

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""


def execute(path1, path2):
    df1 = pandas.read_csv(path1, names=["col1"])
    df2 = pandas.read_csv(path2, names=["col2"])
    df = pandas.concat([df1, df2], axis=1)
    return df.to_csv(sep="\t", header=None, index=False)
