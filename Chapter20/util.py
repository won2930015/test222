#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      won293_root
#
# Created:     03/02/2017
# Copyright:   (c) won293_root 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]

