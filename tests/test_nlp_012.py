#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_012
import subprocess


def test_col1():
    arg1 = 1
    arg2 = '../work/popular-names.txt'
    cmd = f'cut -f {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_012.execute(arg2, arg1)
    assert(expected == actual)


def test_col2():
    arg1 = 2
    arg2 = '../work/popular-names.txt'
    cmd = f'cut -f {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = res.stdout
    actual = nlp_012.execute(arg2, arg1)
    assert(expected == actual)
