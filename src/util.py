#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import os
import subprocess


def unix_cmd(cmd):
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return str(res.stdout)


def expected_file(testpy, suffix="txt"):
    path = os.path.abspath(testpy).removesuffix(".py") + "." + suffix
    with open(path, "rt") as f:
        return f.read()


def tsv2dict(tsv):
    dict = {}
    for li in tsv.splitlines():
        e = li.split("\t")
        if len(e) == 2:
            dict[e[0]] = e[1]
    return dict


def list2text(list):
    return "\n".join(list) + "\n"


def matrix2tsv(matrix):
    return "\n".join([f"{li[0]}\t{li[1]}" for li in matrix]) + "\n"


def dict2tsv(dict):
    return "\n".join([f"{k}\t{v}" for k, v in dict.items()]) + "\n"
