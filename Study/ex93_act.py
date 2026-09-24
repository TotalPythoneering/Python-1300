#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex93_act.py
# AUTHOR: Randall Nagy
# File: ex93_act.py
#

import re

SOURCE = "o Make Bed\n" + \
         "- Brush Teeth\n" + \
         "x Cook Breakfast\n" + \
         "o Make Lunch\n"

source2 = re.subn('^[-x](?= )', '[done]\t',
                  SOURCE, 5, re.M)
source2 = re.subn('^o(?= )', '[todo]\t',
                  str(*source2[0:-1]), 5, re.M)
for info in source2[0:-1]:
    print(info)
