#!/usr/bin/env python3

__version__ = "0.1.0"

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


def execute(arg1, arg2):
    return "".join([i + j for i, j in zip(arg1, arg2)])
