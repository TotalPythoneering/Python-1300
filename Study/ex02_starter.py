#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex02_starter.py
# AUTHOR: Randall Nagy
# File: ex02_starter.py
#

import re

SOURCE = 'test'
demo = re.compile('t')
print('1:', demo.match(SOURCE))
demo = re.compile('e')
print('2:', demo.match(SOURCE))

