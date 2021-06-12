#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

def execute(path):
    with open(path, 'r') as f:
        return f.read().replace('\t', ' ')
