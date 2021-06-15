#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nlp_008

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def test_cipher():
    arg = "paraparaparadise"
    expected = "kzizkzizkzizwrhv"
    actual = nlp_008.cipher(arg)
    print(actual)
    assert expected == actual


def test_decipher():
    arg = "paraparaparadise"
    expected = "paraparaparadise"
    actual = nlp_008.cipher(nlp_008.cipher(arg))
    print(actual)
    assert expected == actual
