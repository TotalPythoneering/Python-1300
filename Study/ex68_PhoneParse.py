#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex68_PhoneParse.py
# AUTHOR: Randall Nagy
# File: ex68_PhoneParse.py
#

import re

SOURCE = "123-456-7890\n" + \
         "ABC-456-7890\n" + \
         "666-555-4321\n" + \
         "555-666-4561\n"

print('All phones with NXX = 456:')
for regx in '\S+-456-\S+',\
    '\w+-(456)-\S+',\
    '(\S+-)(456)-(\S+)':
    for hit in re.finditer(regx, SOURCE):
        if not hit.groups():
            print(regx, hit.group(), sep='\t')
        else:
            print(regx, hit.groups(), sep='\t')

print("Phones ending in '0' or '1'")
for regx in '\S*[01]', '\S*(0|1)$':
    for hit in re.finditer(regx, SOURCE, re.M):
        print(regx, hit.group(), sep=': ')

print("Phones ending in '0'")
for regx in '\S*[0]$', '\S*0$':
    for hit in re.finditer(regx, SOURCE, re.M):
        print(regx, hit.group(), sep=': ')   
