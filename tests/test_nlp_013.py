#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_013
import subprocess


def test_execute():
    arg1 = '../work/col1.txt'
    arg2 = '../work/col2.txt'
    cmd = f'paste {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_013.execute(arg1, arg2)
    assert(expected == actual)
