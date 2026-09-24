#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex00_starter.py
# AUTHOR: Randall Nagy
# File: ex00_starter.py
#

import re

PTRN = 'test'
demo = re.compile(PTRN)
help(demo)
print(demo.match(PTRN))
print(demo.match(PTRN).group())
print(demo.match('mystuff'))
