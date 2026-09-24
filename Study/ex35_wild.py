#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex35_wild.py
# AUTHOR: Randall Nagy
# File: ex35_wild.py
#

import re

for cx in '\n', '\r', '\t':
    for match in re.finditer(cx,'t\r\t\nt'):
        print(match)
    

