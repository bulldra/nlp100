#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import subprocess


def unix_cmd(cmd):
    res = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return str(res.stdout)
