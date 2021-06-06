#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''

'''
任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法．
特に，nが1の場合をユニグラム（uni-gram），
2の場合をバイグラム（bi-gram），3の場合をトライグラム（tri-gram）と呼ぶ．

https://kotobank.jp/word/Nグラム-1702302
'''


def n_gram(arg, n):
    return [arg[i:i + n] for i in range(len(arg) - n + 1)]


def char_bi_gram(arg):
    return n_gram(arg, 2)


def word_bi_gram(arg):
    return n_gram(arg.split(' '), 2)
