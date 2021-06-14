#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_011
import util

'''
11. タブをスペースに置換Permalink
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

def test_sed():
    arg = './work/popular-names.txt'
    expected = util.unix_cmd(f'sed -e "s/\t/ /g" {arg}')
    actual = nlp_011.execute(arg)
    assert(expected == actual)

def test_tr():
    arg = './work/popular-names.txt'
    expected = util.unix_cmd(f'cat {arg} | tr "\t" " "')
    actual = nlp_011.execute(arg)
    assert(expected == actual)

def test_expand():
    arg = './work/popular-names.txt'
    expected = util.unix_cmd(f'expand -t 1 {arg}')
    actual = nlp_011.execute(arg)
    assert(expected == actual)
