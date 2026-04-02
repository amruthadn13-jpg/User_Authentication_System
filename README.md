## 🔐 User Authentication System (File Handling)

---

## 📌 Overview

This project is a **User Authentication System** built using Python and File Handling.
It allows users to:

* Register new accounts
* Login securely
* Change password
* Delete account

All user data is stored in a file (`users.txt`) in a structured format.

---

## 🚀 Features

✔ User Registration
✔ User Login
✔ Change Password
✔ Delete User Account
✔ Prevent Duplicate Usernames
✔ File-based Data Storage
✔ Error Handling (File Not Found, Invalid Data)

---

## 🧠 Concepts Used

* File Handling (`r`, `w`, `a`)
* Functions
* Loops (`while`)
* Conditional Statements
* String Manipulation (`split`, `strip`)
* Exception Handling (`try-except`)

---

## 📂 File Structure

```
project_folder/
│
├── file_handling_day29.py
├── users.txt
```

---

## 📄 Data Format (users.txt)

User data is stored in this format:

```
username,password
```

### Example:

```
Amrutha,Amrutha@18
Harsha,Harsha@2004
Padma,Padma@87
```

---

## ⚙️ How It Works

### 🔹 1. Register

* Takes username and password
* Checks if username already exists
* Stores data in `users.txt`

---

### 🔹 2. Login

* Reads all users from file
* Compares username and password
* Displays success or failure message

---

### 🔹 3. Change Password

* Verifies old password
* Updates with new password

---

### 🔹 4. Delete User

* Verifies credentials
* Removes user from file

---

## ❗ Error Handling

* Handles missing file (`FileNotFoundError`)
* Skips invalid or empty lines
* Prevents program crashes

---

## 💡 Example Output

```
___ User System ___
1. Register
2. Login
3. Change Password
4. Delete User
5. Exit

Enter your choice: 2
Enter username: Amrutha
Enter password: Amrutha@18

Login successful!
```

---

## 🔥 Key Learning

| Concept            | Description                 |
| ------------------ | --------------------------- |
| File Handling      | Store and retrieve data     |
| Authentication     | Validate user credentials   |
| Data Processing    | Use `split()` and `strip()` |
| Exception Handling | Prevent crashes             |

---

## 🔮 Future Improvements

* Password masking (security)
* Use JSON instead of text file
* Add GUI (Tkinter / Web App)
* Encrypt passwords
* Add admin panel

---

## 🙌 Conclusion

This project simulates a **real-world login system** and strengthens understanding of:

* File handling
* User validation
* Error handling

---

⭐ Keep learning, keep building!

**Author**
Amrutha D N
