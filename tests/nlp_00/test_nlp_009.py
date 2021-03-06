#!/usr/bin/env python3

__version__ = "0.1.0"

from nlp_00 import nlp_009

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば”I couldn’t believe that
I could actually understand what I was reading :
the phenomenal power of the human mind .”）を
与え，その実行結果を確認せよ．
"""


def test_execute():
    arg = "I couldn’t believe that \
I could actually understand what I was reading : \
the phenomenal power of the human mind ."
    expected = "I could believe that \
I human couldn’t actually what I was understand : \
the power phenomenal of the reading mind ."
    actual = nlp_009.execute(arg, seed=1)
    print(actual)
    assert expected == actual
