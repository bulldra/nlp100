#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""


def execute(path):
    with open(path, "r") as f:
        return len(f.read().splitlines())
