#!/usr/bin/env python3
"""Defines a function that returns the log message obfuscated"""
import re
from typing import List


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
