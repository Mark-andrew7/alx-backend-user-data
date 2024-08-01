#!/usr/bin/env python3
"""
Module to filter and obfuscate log messages.
"""

from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.
    """
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message

def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object with the name 'user_data'.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Constructor method to initialize the RedactingFormatter object.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using `filter_datum`.
        """
        return filter_datum(
            list(record.__dict__.keys()), self.REDACTION, super(
                RedactingFormatter, self).format(record), self.SEPARATOR)