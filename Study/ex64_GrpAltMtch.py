#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex64_GrpAltMtch.py
# AUTHOR: Randall Nagy
# File: ex64_GrpAltMtch.py
#

import re

SOURCE ="randall.nagy@soft9000.com\n" + \
	"john-juan@foo.edu\n" + \
	"tina.dax@mon.org\n"

regx = '(\S+@)(\w+).(com|org|gov|edu)'
for hit in re.finditer(regx, SOURCE):
    print(hit.groups())



    

