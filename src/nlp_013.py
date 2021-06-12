#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"


def execute(path1, path2):
    with open(path1, 'r') as f1:
        with open(path2, 'r') as f2:
            ff1 = f1.read().splitlines()
            ff2 = f2.read().splitlines()
            return '\n'.join([
                f'{fff1}\t{fff2}' for fff1, fff2 in zip(ff1, ff2)
            ]) + '\n'
