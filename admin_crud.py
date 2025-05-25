import sqlite3
import hashlib

DB_FILE = "users.db"

# Function to create a new user
def create_user(email, password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

# Function to read all users
def read_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to update a user's email or password
def update_user(user_id, new_email=None, new_password=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if new_email:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    if new_password:
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))
    conn.commit()
    print("User updated successfully!")
    conn.close()

# Function to delete a user
def delete_user(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("User deleted successfully!")
    conn.close()

# Admin menu for CRUD operations
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            create_user(email, password)
        elif choice == "2":
            users = read_users()
            print("\nUsers:")
            for user in users:
                print(f"ID: {user[0]}, Email: {user[1]}")
        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            new_email = input("Enter new email (leave blank to skip): ")
            new_password = input("Enter new password (leave blank to skip): ")
            update_user(user_id, new_email if new_email else None, new_password if new_password else None)
        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == "5":
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    admin_menu()