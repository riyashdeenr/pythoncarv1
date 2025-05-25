import sqlite3
from passlib.context import CryptContext
import bcrypt

# Check if bcrypt is installed and set the version
if not hasattr(bcrypt, '__about__'):
    bcrypt.__about__ = type('about', (object,), {'__version__': bcrypt.__version__})


# Initialize Passlib context for bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize SQLite database
def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Create a table for user registration
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Function to register a user
def register_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Hash the password using bcrypt
    hashed_password = pwd_context.hash(password)

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

# Function to verify a user's password
def verify_password(stored_password, provided_password):
    return pwd_context.verify(provided_password, stored_password)

