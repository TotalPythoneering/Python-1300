#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex37_Nuller.py
# AUTHOR: Randall Nagy
# File: ex37_Nuller.py
#

import re
data = '1\n2\n'
for ptrn in '^', '.', '$':
    for m in re.finditer(ptrn, data, re.M):
        print(m)

