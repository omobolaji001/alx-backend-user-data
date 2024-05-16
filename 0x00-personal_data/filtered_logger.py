#!/usr/bin/env python3
"""Defines a function that returns the log message obfuscated"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        obfuscated = filter_datum(self.fields, self.REDACTION,
                                  message, self.SEPARATOR)
        return obfuscated


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the obfuscated log message

    Args:
                fields (List[str]): list of string representing
                                    all fields to obfuscate.
                redaction (str): a string representing by what the field
                                 will be obfuscated.
                message (str): a string representing the log line.
                separator (str): a string representing by which character
                                 is separating all fields in the log line.
    Returns:
                str: returns the obfuscated message.
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)

    return message
