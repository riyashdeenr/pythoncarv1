from db_utils import initialize_db, register_user

# Example usage
if __name__ == "__main__":
    initialize_db()
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    register_user(email, password)

# This code initializes a SQLite database and registers a user with email and password.
# It hashes the password for security and handles email uniqueness. 

