#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_015
import subprocess


def test_tail1():
    arg1 = 1
    arg2 = '../work/popular-names.txt'
    cmd = f'tail -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)


def test_tail3():
    arg1 = 3
    arg2 = '../work/popular-names.txt'
    cmd = f'tail -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)


def test_tail10():
    arg1 = 10
    arg2 = '../work/popular-names.txt'
    cmd = f'tail -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_015.execute(arg2, arg1)
    assert(expected == actual)
