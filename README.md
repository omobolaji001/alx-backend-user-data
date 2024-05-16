# Secure Log Management and Data Handling Project

## Project Overview

This project provides a comprehensive solution for secure log management and data handling, focusing on obfuscating Personally Identifiable Information (PII) within logs, securely managing user passwords, and safely connecting to databases without exposing sensitive credentials. It incorporates regular expressions for data filtering, logging with customized formatting, secure password handling using hashing, and database interactions safeguarded by environment variables.

### Key Features:

- **Regex-based Data Obfuscation:** Utilizes regular expressions to filter and obfuscate specified fields in log messages, ensuring that sensitive information like passwords and dates of birth are not exposed in plain text.
- **Advanced Logging Mechanism:** Implements a custom logging formatter that redacts PII data from log records, maintaining privacy and compliance with data protection regulations.
- **Secure Password Storage:** Offers a mechanism for hashing passwords before storage, using the bcrypt library to salt and hash user passwords, enhancing security against brute-force attacks and unauthorized access.
- **Database Connection Security:** Connects to databases using credentials stored in environment variables, preventing hard-coded credentials from being exposed in the codebase or version control.
- **PII Filtering in Database Outputs:** Filters sensitive information from database query results before logging, ensuring that logged data does not reveal PII.

## Installation

To get started with this project, clone the repository from GitHub and install the necessary dependencies.

1. **Clone the Repository:**

   ```
   git clone https://github.com/shazaaly/alx-backend-user-data.git
   cd alx-backend-user-data
   ```

2. **Install Dependencies:**

   This project requires Python 3.6 or later. Ensure you have Python and pip installed on your system. Then, install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

   This will install `mysql-connector-python` for database interactions and `bcrypt` for password hashing.

## Usage

This section outlines how to use the main functionalities of the project.

### 1. Obfuscating Data in Logs

Use the `filter_datum` function to obfuscate specific fields in a log message. Here's how to use it in your Python code:

```python
from filtered_logger import filter_datum

fields = ["password", "date_of_birth"]
message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
obfuscated_message = filter_datum(fields, 'xxx', message, ';')
print(obfuscated_message)
```

### 2. Logging with Redacted PII

To create a logger that automatically redacts specified PII fields, use the `RedactingFormatter` class:

```python
import logging
from filtered_logger import get_logger

logger = get_logger()
logger.info("User login: email=bob@dylan.com; password=verysecret;")
```

### 3. Secure Database Connection

To connect to a database securely, use the `get_db` function. Ensure you have set the required environment variables (`PERSONAL_DATA_DB_USERNAME`, `PERSONAL_DATA_DB_PASSWORD`, `PERSONAL_DATA_DB_HOST`, and `PERSONAL_DATA_DB_NAME`):

```python
from filtered_logger import get_db

db_connection = get_db()
# Use db_connection as needed
```

### 4. Password Hashing and Verification

To hash and verify passwords securely, use the `hash_password` and `is_valid` functions:

```python
from encrypt_password import hash_password, is_valid

password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)

# Verify the password
print(is_valid(hashed_password, password))
```

## Contributing

Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

All rights reserved to ALX
