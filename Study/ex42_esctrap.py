#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex42_esctrap.py
# AUTHOR: Randall Nagy
# File: ex42_esctrap.py
#

import re

SOURCE ="ABC-346\n" + \
	"123-DEF\n" + \
	"DEF\n" + "456"

for mask in '^\d', '^\D':
    print(re.findall(mask, SOURCE,
            re.MULTILINE))
  

