#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex32_wild.py
# AUTHOR: Randall Nagy
# File: ex32_wild.py
#

import re

SOURCE ="This is a test\n" + \
	"RE’s are neat\n" + \
	"If this is ok\n" + \
	"Then life be sweet"

for mask in '^t', 't$':
    print(re.findall(mask, SOURCE,
            re.MULTILINE | re.IGNORECASE))

    

