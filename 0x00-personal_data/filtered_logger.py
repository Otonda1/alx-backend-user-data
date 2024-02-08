#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this module is used to filter the data in the log file


import re

def filter_datum(fields, redaction, message, separator):
    #function to filter the data in the log file using re
    for field in fields:
        pattern = re.compile(r'\b' + re.escape(field) + r'=[^' + re.escape(separator) + r']*')
        message = re.sub(pattern, field + '=' + redaction, message)
    return message
