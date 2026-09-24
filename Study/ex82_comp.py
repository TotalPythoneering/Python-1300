#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex82_comp.py
# AUTHOR: Randall Nagy
# File: ex82_comp.py
#

import re

SOURCE = "123-456-7890\n" + \
         "ABC-456-7890\n" + \
         "666-555-4321\n" + \
         "555-666-4561\n"

ptrn = re.compile('5{1,3}')
source2 = ptrn.subn('!', SOURCE, 2)
print(source2)    

source2 = ptrn.sub('!', SOURCE)
print(source2)    
