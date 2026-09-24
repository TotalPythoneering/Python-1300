#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex25_wild.py
# AUTHOR: Randall Nagy
# File: ex25_wild.py
#

import re

SOURCE = 'test'
MASK = '.es.'
print(re.match(MASK, SOURCE))
print(re.search(MASK, SOURCE))
   

