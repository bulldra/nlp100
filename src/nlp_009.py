#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import random

'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば”I couldn’t believe that
I could actually understand what I was reading :
the phenomenal power of the human mind .”）を
与え，その実行結果を確認せよ．
'''


def execute(arg, seed=None):
    if seed is not None:
        random.seed(seed)

    term = arg.split(' ')
    rand = [i for i in range(len(term)) if is_rand(term, i)]
    random.shuffle(rand)

    return ' '.join([
        term[rand.pop()] if is_rand(term, i) else term[i]
        for i in range(len(term))
    ])


def is_rand(term, i):
    return i not in (0, len(term) - 1) and len(term[i]) > 4
