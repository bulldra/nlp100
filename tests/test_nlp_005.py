#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nlp_005

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


def test_char_bi_gram():
    arg = 'I am an NLPer'
    expected = [
        'I ', ' a', 'am', 'm ', ' a', 'an', 'n ',
        ' N', 'NL', 'LP', 'Pe', 'er'
    ]
    actual = nlp_005.char_bi_gram(arg)
    print(actual)
    assert(expected == actual)


def test_word_bi_gram():
    arg = 'I am an NLPer'
    expected = [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    actual = nlp_005.word_bi_gram(arg)
    print(actual)
    assert(expected == actual)
