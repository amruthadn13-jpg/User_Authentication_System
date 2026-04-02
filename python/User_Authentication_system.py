FILE_NAME = "users.txt"


def register():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and Password cannot be empty!")
        return

    try:
        with open(FILE_NAME, "r") as file:
            users = file.readlines()

        for user in users:
            user = user.strip()
            if not user:
                continue

            parts = user.split(",")
            if len(parts) != 2:
                continue

            if username == parts[0].strip():
                print("Username already exists!")
                return

    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")

    print("User registered successfully!")


def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        with open(FILE_NAME, "r") as file:
            users = file.readlines()

        found = False

        for user in users:
            user = user.strip()

            if not user:
                continue

            parts = user.split(",")

            if len(parts) != 2:
                continue

            u = parts[0].strip()
            p = parts[1].strip()

            if username == u and password == p:
                print("Login successful!")
                found = True
                break

        if not found:
            print("Invalid credentials!")

    except FileNotFoundError:
        print("No users found!")


def change_password():
    username = input("Enter username: ").strip()
    old_password = input("Enter old password: ").strip()

    try:
        with open(FILE_NAME, "r") as file:
            users = file.readlines()

        updated_users = []
        found = False

        for user in users:
            user = user.strip()
            if not user:
                continue

            parts = user.split(",")
            if len(parts) != 2:
                continue

            u, p = parts

            if username == u and old_password == p:
                new_password = input("Enter new password: ").strip()
                updated_users.append(f"{username},{new_password}\n")
                found = True
                print("Password changed successfully!")
            else:
                updated_users.append(user + "\n")

        if not found:
            print("Invalid username or password!")

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_users)

    except FileNotFoundError:
        print("No users found!")


def delete_user():
    username = input("Enter username to delete: ").strip()
    password = input("Enter password: ").strip()

    try:
        with open(FILE_NAME, "r") as file:
            users = file.readlines()

        updated_users = []
        found = False

        for user in users:
            user = user.strip()
            if not user:
                continue

            parts = user.split(",")
            if len(parts) != 2:
                continue

            u, p = parts

            if username == u and password == p:
                found = True
                print("User deleted successfully!")
                continue
            else:
                updated_users.append(user + "\n")

        if not found:
            print("Invalid credentials!")

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_users)

    except FileNotFoundError:
        print("No users found!")


# Main Menu
while True:
    print("\n___ User System ___")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        change_password()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        print("System closed!")
        break

    else:
        print("Invalid choice!")
