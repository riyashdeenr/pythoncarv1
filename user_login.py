from db_utils import initialize_db, verify_password
import sqlite3

# Function to authenticate a user
def authenticate_user(email, provided_password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result and verify_password(result[0], provided_password):
        return True
    return False

# Login page
def login_page():
    print("Welcome to the Login Page!")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if authenticate_user(email, password):
        print("Login successful! Welcome!")
    else:
        print("Invalid email or password. Please try again.")
        

# Example usage
if __name__ == "__main__":
    initialize_db()  # Ensure the database is initialized
    login_page()