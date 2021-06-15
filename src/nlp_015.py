#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""


def execute(path, tail):
    with open(path, "r") as f1:
        return "\n".join(f1.read().splitlines()[-tail:]) + "\n"
