#!/usr/bin/env python3
"""
Filter Logging Information for security
"""
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate Message string"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Fomrat Filtered Message """
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.FIELDS, self.REDACTION, msg, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Mock Instance of getLogger
    return: <class 'logging.Logger'>
    """
    logger = logging.getLogger('user_data')
    logger.propagate = False
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(RedactingFormatter.FORMAT)
    logger.addHandler(console_handler)
    return logger
