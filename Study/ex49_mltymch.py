#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex49_mltymch.py
# AUTHOR: Randall Nagy
# File: ex49_mltymch.py
#

import re

SOURCE ="Good 4 you 2!\n"
print(SOURCE)
# + - One or More Alpha Numeric(s):
for match in re.finditer('\w+', SOURCE):
    print(match)

### * - Zero or More Alpha Numeric(s):
##for match in re.finditer('\w*', SOURCE):
##    print(match)

### ? - Zero or One Alpha Numeric(s):  
##for match in re.finditer('\w?', SOURCE):
##    print(match)

