#!/usr/bin/env python3

__version__ = "0.1.0"

import gzip
import json

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

https://docs.python.org/ja/3.9/library/gzip.html
"""


def execute(input):
    with gzip.open(input, mode="rt", encoding="utf-8") as f:
        for json_text in f.read().splitlines():
            article = json.loads(json_text)
            if article["title"] == "イギリス":
                return article["text"] + "\n"
