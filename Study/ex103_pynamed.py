#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex103_pynamed.py
# AUTHOR: Randall Nagy
# File: ex103_pynamed.py
#

import re

comp = re.compile(
'([-.+%_a-z0-9]+)@  # USER ID\n\
(.*[a-z0-9])*.      # DOMAIN NAME\n\
([a-z]{2,4})        # DOMAIN TYPE',
re.I | re.VERBOSE)

SOURCE = "Test R.Nagy@Soft9000.com\n" + \
         "or Bob-White@BirdTime.gov\n" + \
         "There is foo@bar.net\n" + \
         "or nut_job@ForTheFun.biz\n"

for phone in comp.finditer(SOURCE):
    for ss, group in enumerate(phone.groups(), 1):
        print(ss,group)
    print('*'*5)


