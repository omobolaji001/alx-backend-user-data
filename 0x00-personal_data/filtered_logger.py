#!/usr/bin/env python3
"""Defines a function that returns the log message obfuscated"""
import re
from typing import List
import logging
PII_FIELDS = ("email", "phone", "ssn", "password", "ip")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Instantiates RedactingFormatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record and obfuscate sensitive data.

        Args:
                record (logging.LogRecord): contains the log message

        Returns:
                str: The formatted log message with sensitive data obfuscated
        """
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


def get_logger() -> logging.Logger:
    """Returns a logger for user data"""
    logger = logging.getLogger('user_data')
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    return logger.addHandler(handler)
