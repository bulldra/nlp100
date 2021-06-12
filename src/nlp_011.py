#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"


def execute(path):
    with open(path, 'r') as f:
        return f.read().replace('\t', ' ')
