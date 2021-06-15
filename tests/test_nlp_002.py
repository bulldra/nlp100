#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nlp_002

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


def test_execute():
    arg1 = "パトカー"
    arg2 = "タクシー"
    excepted = "パタトクカシーー"
    actual = nlp_002.execute(arg1, arg2)
    print(actual)
    assert excepted == actual
