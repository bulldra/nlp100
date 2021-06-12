#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_015
import subprocess


def test_split1():
    arg1 = 1
    arg2 = '../work/popular-names.txt'
    cmd = f'split -n {arg1} {arg2} ../work/split_expected1_'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    print(expected)
    #actual = nlp_015.execute(arg2, arg1)
    #assert(expected == actual)


def test_split3():
    arg1 = 3
    arg2 = '../work/popular-names.txt'
    cmd = f'split -n {arg1} {arg2} ../work/split_expected3_'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    print(expected)
    #actual = nlp_015.execute(arg2, arg1)
    #assert(expected == actual)
