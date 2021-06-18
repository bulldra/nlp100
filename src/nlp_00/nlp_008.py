#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(arg):
    return "".join([chr(219 - ord(s)) if s.islower() else s for s in arg])
