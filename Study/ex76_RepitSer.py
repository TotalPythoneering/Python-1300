#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex76_RepitSer.py
# AUTHOR: Randall Nagy
# File: ex76_RepitSer.py
#

import re

SOURCE = "123-456-7890\n" + \
         "ABC-456-7890\n" + \
         "666-555-4321\n" + \
         "555-666-4561\n"

# Match '666':
for hit in re.finditer('6{3}', SOURCE):
    print(hit)
print()
# Match '666' or '555':
for hit in re.finditer('(5|6){3}', SOURCE):
    print(hit)
print()
# Match 1-3 '6's or '5's:
for hit in re.finditer('(5|6){1,3}', SOURCE):
    print(hit)    
