#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_015
import util

'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''

def test_tail1():
    arg1 = 1
    arg2 = './work/popular-names.txt'
    expected = util.unix_cmd(f'tail -n {arg1} {arg2}')
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)


def test_tail3():
    arg1 = 3
    arg2 = './work/popular-names.txt'
    expected = util.unix_cmd(f'tail -n {arg1} {arg2}')
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)


def test_tail10():
    arg1 = 10
    arg2 = './work/popular-names.txt'
    expected = util.unix_cmd(f'tail -n {arg1} {arg2}')
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)
