#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: review_non_ranged.py
# AUTHOR: Randall Nagy
# File: review_non_ranged.py
#

import re

SOURCE = "aaabbbccc"

re_set = {
    'greedy+':'b{1,3}',
    'nogreed+':'b{1,3}?',
    }
    
for rex in re_set:
    print(rex, re.findall(re_set[rex], SOURCE))



