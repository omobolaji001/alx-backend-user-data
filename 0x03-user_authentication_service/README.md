# User Authentication Service

This project is part of the ALX Africa software engineering program and aims to provide a user authentication service using Flask and SQLAlchemy.

## Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Tasks](#tasks)
4. [Usage](#usage)

## 1. Overview

This repository contains the implementation for a user authentication service. The service is built using Flask and SQLAlchemy, providing functionality such as user registration, login, session management, and password reset.

## 2. Setup

To set up the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/alx-backend-user-data.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database settings in `config.py`.

4. Run the application:

   ```bash
   python app.py
   ```

## 3. Tasks

The project is organized into tasks based on the ALX Africa software engineering program curriculum. Each task corresponds to specific topics and skills that you've learned during the program.

I apologize for the oversight. Let me continue with the rest of the tasks:

### Task 4: Update User

Implement the update_user method in the `0x03-user_authentication_service/db.py` file. This method should update a user's attributes in the database. Follow the provided instructions.

### Task 5: Hash Password

Define the _hash_password method in the `0x03-user_authentication_service/auth.py` file. This method should hash a password using bcrypt.hashpw. Follow the provided instructions.

### Task 6: Register User

Implement the register_user method in the `0x03-user_authentication_service/auth.py` file. This method should register a new user, hash the password, and save the user to the database. Follow the provided instructions.

### Task 7: Basic Flask App

Set up a basic Flask app with a single GET route ("/") in the `0x03-user_authentication_service/app.py` file. Use flask.jsonify to return a JSON payload. Follow the provided instructions.

### Task 8: Register User Endpoint

Implement the /users endpoint in the `0x03-user_authentication_service/app.py` file. This endpoint should register a user and respond with JSON payloads based on success or failure. Follow the provided instructions.

### Task 9: Credentials Validation

Implement the valid_login method in the `0x03-user_authentication_service/auth.py` file. This method should validate user credentials and return a boolean. Follow the provided instructions.

### Task 10: Generate UUIDs

Implement the _generate_uuid function in the `0x03-user_authentication_service/auth.py` file. This function should return a string representation of a new UUID. Follow the provided instructions.

### Task 11: Get Session ID

Implement the create_session method in the `0x03-user_authentication_service/auth.py` file. This method should create a new session for a user and return the session ID. Follow the provided instructions.

### Task 12: Log In

Implement the login function to respond to the POST /sessions route in the `0x03-user_authentication_service/app.py` file. This function should handle user login and session creation. Follow the provided instructions.

### Task 13: Find User by Session ID

Implement the get_user_from_session_id method in the `0x03-user_authentication_service/auth.py` file. This method should find a user based on the session ID. Follow the provided instructions.

### Task 14: Destroy Session

Implement the destroy_session method in the `0x03-user_authentication_service/auth.py` file. This method should update a user's session ID to None. Follow the provided instructions.

### Task 15: Log Out

Implement the logout function to respond to the DELETE /sessions route in the `0x03-user_authentication_service/app.py` file. This function should handle user logout by destroying the session. Follow the provided instructions.

### Task 16: User Profile

Implement the profile function to respond to the GET /profile route in the `0x03-user_authentication_service/app.py` file. This function should return a user's profile information based on the session ID. Follow the provided instructions.

### Task 17: Generate Reset Password Token

Implement the get_reset_password_token method in the `0x03-user_authentication_service/auth.py` file. This method should generate a reset password token for a user. Follow the provided instructions.

### Task 18: Get Reset Password Token

Implement the /reset_password endpoint in the `0x03-user_authentication_service/app.py` file. This endpoint should handle requests to generate and retrieve reset password tokens. Follow the provided instructions.

### Task 19: Update Password

Implement the update_password method in the `0x03-user_authentication_service/auth.py` file. This method should update a user's password based on a reset token. Follow the provided instructions.

### Task 20: Update Password Endpoint

Implement the PUT /reset_password route in the `0x03-user_authentication_service/app.py` file. This route should handle requests to update a user's password using a reset token. Follow the provided instructions.
