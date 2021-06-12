#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_010
import subprocess


def test_execute():
    arg = '../work/popular-names.txt'
    cmd = f'cat {arg} | wc -l'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = res.stdout.rstrip()
    actual = str(nlp_010.execute(arg))
    assert(expected == actual)
