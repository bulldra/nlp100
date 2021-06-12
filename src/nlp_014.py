#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"


def execute(path, head):
    with open(path, 'r') as f1:
        return '\n'.join(f1.read().splitlines()[:head]) + '\n'
