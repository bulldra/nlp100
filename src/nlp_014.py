#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""


def execute(path, head):
    with open(path, "r") as f1:
        return "\n".join(f1.read().splitlines()[:head]) + "\n"
