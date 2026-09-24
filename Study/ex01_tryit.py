#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex01_tryit.py
# AUTHOR: Randall Nagy
# File: ex01_tryit.py
#

import re

comp = re.compile('e')

SOURCE = 'we flee key'
print(SOURCE)
print("1:", comp.findall(SOURCE))
print("2:", re.findall('e', SOURCE))

   

