#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import nlp_007

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ
"""


def test_execute():
    arg1 = 12
    arg2 = "気温"
    arg3 = 22.4
    expected = "12時の気温は22.4"
    actual = nlp_007.execute(arg1, arg2, arg3)
    print(actual)
    assert expected == actual
