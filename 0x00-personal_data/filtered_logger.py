#!/usr/bin/env python3
"""
Filter User Information
"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter Information"""
    msg = message
    for field in fields:
        msg = re.sub(r'{}=(.*?){}'.format(field, separator),
                     '{}={}{}'.format(field, redaction, separator), msg)
    return msg
