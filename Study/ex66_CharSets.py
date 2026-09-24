#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex66_CharSets.py
# AUTHOR: Randall Nagy
# File: ex66_CharSets.py
#

import re

SOURCE ="The * spangled banner?"

print(SOURCE)
##for hit in re.finditer('[*?]', SOURCE):
##    print(hit)

for hit in re.finditer('[*?a-d]', SOURCE):
    print(hit)
    

