#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import os
import subprocess


def unix_cmd(cmd):
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return str(res.stdout)


def build_expected_path(testpy, suffix="txt"):
    return os.path.abspath(testpy).removesuffix(".py") + "." + suffix


def list2text(list):
    return "\n".join(list) + "\n"


def matrix2tsv(matrix):
    return "\n".join([f"{li[0]}\t{li[1]}" for li in matrix]) + "\n"


def dict2tsv(dict):
    return "\n".join([f"{k}\t{v}" for k, v in dict.items()]) + "\n"
