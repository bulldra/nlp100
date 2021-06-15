#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import filecmp

import nlp_016
import util

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""


def test_split1():
    input = "./work/popular-names.txt"
    num = 1
    exp_out = f"./work/split_expected_{num}_"
    act_out = f"./work/split_actual_{num}_"
    util.unix_cmd(
        f"split -l $((`cat {input} | wc -l` / {num} + 1 )) {input} -d {exp_out}"
    )
    nlp_016.execute(input, num, act_out)
    assert filecmp.cmp(f"{exp_out}00", f"{act_out}00")


def test_split3():
    input = "./work/popular-names.txt"
    num = 3
    exp_out = f"./work/split_expected_{num}_"
    act_out = f"./work/split_actual_{num}_"
    util.unix_cmd(
        f"split -l $((`cat {input} | wc -l` / {num} + 1 )) {input} -d {exp_out}"
    )
    nlp_016.execute(input, num, act_out)
    assert filecmp.cmp(f"{exp_out}00", f"{act_out}00")
    assert filecmp.cmp(f"{exp_out}01", f"{act_out}01")
    assert filecmp.cmp(f"{exp_out}02", f"{act_out}02")


def test_split5():
    input = "./work/popular-names.txt"
    num = 5
    exp_out = f"./work/split_expected_{num}_"
    act_out = f"./work/split_actual_{num}_"
    util.unix_cmd(
        f"split -l $((`cat {input} | wc -l` / {num} + 1 )) {input} -d {exp_out}"
    )
    nlp_016.execute(input, num, act_out)
    assert filecmp.cmp(f"{exp_out}00", f"{act_out}00")
    assert filecmp.cmp(f"{exp_out}01", f"{act_out}01")
    assert filecmp.cmp(f"{exp_out}02", f"{act_out}02")
    assert filecmp.cmp(f"{exp_out}03", f"{act_out}03")
    assert filecmp.cmp(f"{exp_out}04", f"{act_out}04")
