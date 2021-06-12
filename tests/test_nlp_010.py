#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_010
import util

'''
10. 行数のカウントPermalink
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

def test_execute():
    arg = '../work/popular-names.txt'
    expected = util.unix_cmd(f'cat {arg} | wc -l').rstrip()
    actual = str(nlp_010.execute(arg))
    assert(expected == actual)
