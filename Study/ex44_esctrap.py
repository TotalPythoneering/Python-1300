#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex44_esctrap.py
# AUTHOR: Randall Nagy
# File: ex44_esctrap.py
#

import re

SOURCE ="9\n" + "A\n" + " \n"
traps = {'d':'decimal', 's':'space', 'w':'alnum'}
for code in traps:
    mask = '\\' + code
    print(f'{traps[code]:<8s}\t',
          re.findall(mask, SOURCE,
          re.MULTILINE))
    mask = '\\' + code.upper()
    print('Not-' + f'{traps[code]:<8s}\t',
          re.findall(mask, SOURCE,
          re.MULTILINE))
  

