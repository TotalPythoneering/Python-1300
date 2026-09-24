#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex52_mltymch.py
# AUTHOR: Randall Nagy
# File: ex52_mltymch.py
#

import re

SOURCE = "235-ABC\n" + \
         "236-ABD\n" + \
         "237-DSD\n"

print(SOURCE)
print("One or More '23'")
for match in re.finditer('23', SOURCE):
    print(match)

print("One or More Words")
for match in re.finditer('\w+', SOURCE):
    print(match)

print("Zero or One lines ending with 'C'")  
for match in re.finditer('C\n?', SOURCE):
    print(match)

