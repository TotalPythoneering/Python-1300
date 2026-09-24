#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: ex100_pynamed.py
# AUTHOR: Randall Nagy
# File: ex100_pynamed.py
#

# from email.utils import parseaddr

import re

comp = re.compile(
'(?P<NAME>[-.+%_a-z0-9]+)@\
(?P<DOMAIN>.*[a-z0-9])*.\
(?P<DOT>[a-z]{2,4})\W', re.I)

SOURCE = "Test R.Nagy@Soft9000.com\n" + \
         "or Bob-White@BirdTime.gov\n" + \
         "There is foo@bar.net\n" + \
         "or nut_job@ForTheFun.biz\n"

for phone in comp.finditer(SOURCE):
    print("User:",phone.group('NAME'))
    print("Site:",phone.group('DOMAIN'))
    print("Type:",phone.group('DOT'))
    print()


