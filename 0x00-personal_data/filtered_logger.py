#!/usr/bin/env python3
"""
Filter User Information
"""
import logging
import re


def filter_datum(fields, redaction, message, separator) -> str:
    """Filter Information"""
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
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
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.FIELDS, self.REDACTION, msg,
                                    self.SEPARATOR)
