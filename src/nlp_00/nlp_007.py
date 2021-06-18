#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ
"""


def execute(x, y, z):
    return f"{x}時の{y}は{z}"
