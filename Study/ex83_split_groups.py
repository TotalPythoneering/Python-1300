#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex83_split_groups.py
# AUTHOR: Randall Nagy
# File: ex83_split_groups.py
#

import re

SOURCE = "123-456-7890\n" + \
         "ABC-456-7890\n" + \
         "666-555-4321\n" + \
         "555-666-4561\n"

#\s = Whitepace
#\w = Alnum
# Review \w+ -v- \S+ results?
ptrn = '(\S+[01])\n'
for split in re.split(ptrn, SOURCE):
    if len(split) < 1:
        print('null')
    else:
        print(repr(split))
