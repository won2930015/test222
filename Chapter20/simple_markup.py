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

import sys,re
from util import *

print '<html><head><title>...</title><body>'

title=True
for block in blocks(sys.stdin):
    block=re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title=False
    else:
        print '<p>'
        print block
        print '</p>'



