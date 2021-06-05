#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

'''
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might
Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目
の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列
（辞書型もしくはマップ型）を作成せよ．
'''


def execute(arg, first):
    term = arg.split(' ')
    return {
        term[i][:1 if i + 1 in first else 2]: i + 1
        for i in range(len(term))
    }
