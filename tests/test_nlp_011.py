#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_011
import subprocess


def test_execute():
    arg = '../work/popular-names.txt'
    cmd = f'sed -e "s/\t/ /g" {arg}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_011.execute(arg)
    assert(expected == actual)
