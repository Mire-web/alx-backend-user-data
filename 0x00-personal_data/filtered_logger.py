#!/usr/bin/env python3
"""
Filter User Information
"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter Information"""
    for field in fields:
        message = re.sub(r'{}=(.*?){}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator), message)
    return msg
