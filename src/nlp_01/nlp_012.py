#!/usr/bin/env python3

__version__ = "0.1.0"

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""


def execute(field, input, output):
    text = cut(field, input)
    with open(output, "w") as f:
        f.write(text)


def cut(field, path):
    with open(path, "r") as f:
        r = [ff.split("\t")[field - 1] for ff in f.read().splitlines()]
        return "\n".join(r) + "\n"
