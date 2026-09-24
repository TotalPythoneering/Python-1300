#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex98_pynamed.py
# AUTHOR: Randall Nagy
# File: ex98_pynamed.py
#

import re

SOURCE = "123-456-7890\n" + \
         "ABC-456-7890\n" + \
         "666-555-4321\n" + \
         "555-666-4561\n"
    
comp = re.compile(
    '(?P<NPA>\d{3})-(?P<NXX>\d{3})-(?P<LINE>\d{4})'
    )
for phone in comp.finditer(SOURCE):
    print("Line:",phone.group('LINE'))
    print("Exng:",phone.group('NXX'))
    print("Area:",phone.group('NPA'))
    print()


