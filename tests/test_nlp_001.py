#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nlp_001

"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""


def test_execute():
    arg = "パタトクカシーー"
    excepted = "パトカー"
    actual = nlp_001.execute(arg)
    print(actual)
    assert excepted == actual
