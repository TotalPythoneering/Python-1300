#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex94_demo.py
# AUTHOR: Randall Nagy
# File: ex94_demo.py
#

import re

SOURCE = "555|453|123\n" + \
         "123(456)789\n" + \
         "666[456]654\n" + \
         "123{453}626\n"

# Also: (?: ...
for info in re.subn(
    '([|(){}[\]])',
    ', "\\1", ',
    SOURCE, 10):
    print(info)

