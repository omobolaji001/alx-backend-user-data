#!/usr/bin/env python3
"""Defines a function that returns the log message obfuscated"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to MySQL database and returns the connector"""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    db_host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(user=db_username,
                                         password=db_password,
                                         host=db_host,
                                         database=db_name)

    return connection


def main():
    """main entry"""
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names

    for row in cursor:
        message = "".join("{}={};".format(i, v) for i, v in zip(fields, row))
        logger.info(message.strip())

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
