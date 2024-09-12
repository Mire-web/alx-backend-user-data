#!/usr/bin/env python3
"""
Filter User Information
"""
import logging
import re


def filter_datum(fields, redaction, message, separator) -> str:
    """Filter Information"""
    for field in fields:
        message = re.sub(r'{}=(.*?){}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator), message)
    return message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format Logged message"""
        return filter_datum(list(self.FIELDS), self.REDACTION,
                                   str(record), self.SEPARATOR)
