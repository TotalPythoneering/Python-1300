#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex34_esctrap.py
# AUTHOR: Randall Nagy
# File: ex34_esctrap.py
#

import re

SOURCE ="Mr. Big\nLast Times\nBit goods\n"
for match in re.finditer('g$|s$', SOURCE,
      re.MULTILINE): print(match)
  

