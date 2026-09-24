#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1300: Regular
# Expressions''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1300
# DATE: 2019-10-09 15:30:00
# FILE: Review21.py
# AUTHOR: Randall Nagy
# File: Review21.py
#

import re

SOURCE = "Email address is \
Mr_Foo@foo.com and the phone \
is (123) 546-1211. From what \
we know, social numbers are \
123-54-6787 and 321-54-6789."

RFC_NAME = "([\w!#$%&'*+\/=?^_`{|.}~-]+)"
RFC_DOMAIN = "(\S+[-.\w]*)"

re_set = {
    'social':'\d{3}-\d{2}-\d{4}',
    'phone': '\((\d{3})\) ?(\d{3})-(\d{4})',
    'email': f'{RFC_NAME}@{RFC_DOMAIN}'
    }
for rex in re_set:
    print(rex, re.findall(re_set[rex], SOURCE))


