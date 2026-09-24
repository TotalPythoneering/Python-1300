#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex27_esct.py
# AUTHOR: Randall Nagy
# File: ex27_esct.py
#

import re

result = re.finditer('.','t\r\t\nt')
for match in result:
    print(match)
    

