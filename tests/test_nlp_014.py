#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"
import nlp_014
import subprocess


def test_head1():
    arg1 = 1
    arg2 = '../work/popular-names.txt'
    cmd = f'head -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_014.execute(arg2, arg1)
    assert(expected == actual)


def test_head3():
    arg1 = 3
    arg2 = '../work/popular-names.txt'
    cmd = f'head -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_014.execute(arg2, arg1)
    assert(expected == actual)


def test_head10():
    arg1 = 10
    arg2 = '../work/popular-names.txt'
    cmd = f'head -n {arg1} {arg2}'
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    expected = str(res.stdout)
    actual = nlp_014.execute(arg2, arg1)
    assert(expected == actual)
