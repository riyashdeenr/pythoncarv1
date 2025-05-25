
from db_utils import initialize_db, verify_password
from user_login import login_page
# This code demonstrates the use of global variables in Python.
# It defines a global variable `int` and modifies it within a function.
def main():
    global int
    int = 2



if __name__ == "__main__":
    main()
    initialize_db()  # Ensure the database is initialized
    login_page()
    print(int)

# The code defines a global variable 'int' and a function 'main'.print(int)

