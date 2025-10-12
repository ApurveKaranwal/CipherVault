# CipherVault

### A powerful and secure command-line password manager that lets you effortlessly generate strong passwords, store them safely in an encrypted local file, and retrieve them instantly whenever you need, all from the convenience of your terminal.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)



---

### ✨ Features

- **Strong Password Generation:** Create secure, random passwords with customizable length and character types.  
- **Encrypted Storage:** Safely store passwords in a local encrypted file to protect sensitive data.  
- **Quick Retrieval:** Easily fetch saved passwords when you need them.  
- **Command-Line Interface (CLI):** Run CipherVault directly from your terminal for fast and simple use.  
- **Prevents Weak Passwords:** Ensures generated passwords include letters, numbers, and symbols for maximum security.  
- **Optional Randomization:** Let CipherVault randomly pick the most secure password for you.  
- **Lightweight and Portable:** No heavy dependencies—works on any system with Python 3.6+.

---

### 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

#### Prerequisites

You need **Python 3.6 or newer** installed on your system.

#### Installation

1.  **Clone the repository** :

    ```bash
    git clone https://github.com/ApurveKaranwal/CipherVault
    cd CipherVault
    ```

2.  **Install the required dependencies:**

    This project requires the `asyncio` `csv` `pyperclip` `random` `datetime` `string` `os` library.

    So install of them

    example:
    ```bash
    pip install asyncio
    ```

---

### 💡 Usage

The basic command structure is designed to be simple and intuitive.
```bash
python ciphervault.py
```

### 🛠 How CipherVault Works
**1. Adding a New Entry**  
When you add a new password, CipherVault guides you through a few simple prompts:  
- **Password Length:** Choose how long you want your password to be.  
- **Special Characters:** Decide whether to include symbols for stronger passwords.  
- **Email & Platform:** Enter the email and the platform (e.g., Gmail, Facebook) for which you are generating the password.

- ![New Entry](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/new%20entry.png)

**2. Password Generation**  
CipherVault then generates a **strong, random password** based on your choices.

**3. Quick Retrieval**  
Whenever you need it, you can **retrieve your password** by searching for the platform or email, making access fast and convenient. 

### 🔒 Secure Storage

CipherVault ensures that your passwords are **securely stored** in a CSV file.  
Even if someone tries to open the CSV file directly, **they won’t be able to read your passwords**, because all data is encrypted.  
This keeps your sensitive information safe from prying eyes.  

![Encrypted Storage](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/csv.png)

### 📊 Display All Entries
CipherVault can show all your saved passwords in a **clean tabular format**.  
This makes it easy to view all platforms, emails, and their corresponding passwords at a glance.

![Display Table](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/display%20table.png)

---

### ✏️ Update Existing Entry
If you try to add a password for a platform/email that **already exists**, CipherVault will **update the existing entry** instead of creating a duplicate.  
This keeps your password records organized and up-to-date.  
![Update Entry](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/updated%20entry.png)

---

### 🔍 Search for a Specific Entry
You can quickly search for a saved password by **platform or email**.  
CipherVault will retrieve the relevant password so you don’t have to scroll through the entire table.  
![Search Entry](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/specific%20entry.png)

---

### ⚠️ Entry Not Found
If you try to retrieve or update a password for a **platform/email that doesn’t exist**, CipherVault shows a **clear error message**.  
This prevents confusion and keeps the workflow clean.  
![Entry Not Found](https://github.com/ApurveKaranwal/CipherVault/blob/main/images/no%20entry.png)

### 🔐 Security Notes
- All passwords are encrypted in the CSV file.  
- Do not share your local CSV file or encryption key.  
- Use strong master passwords if you plan to add one in future versions.


### 🤝 Contributing to CipherVault

We’re thrilled that you’re considering contributing to **CipherVault**!  
Whether it’s reporting a bug, suggesting a feature, or writing code — your efforts are highly valued.

---

## 🐛 Reporting Bugs

If you find a bug, please help us by creating a detailed issue.  
When submitting a bug report, include:

- A clear, descriptive title.  
- The exact steps to reproduce the issue.  
- The expected behavior and the actual behavior.  
- Your Python version and operating system.

---

## ✨ Suggesting Features

If you have an idea for a new feature or enhancement, feel free to open an issue to discuss it.  
This helps ensure that we’re all aligned before you spend time writing code.

---

## 🛠 Submitting Code Changes

To contribute code, please follow this standard workflow:

1. **Fork** the repository on GitHub.

2. **Clone** your forked repository locally:
   ```bash
   git clone https://github.com/ApurveKaranwal/CipherVault.git
   ```
   

3. Create a new, descriptive branch for your feature or fix:
```bash
   git checkout -b feature/your-awesome-feature
   ```

4. Make your changes.

5. Ensure your code adheres to standard Python formatting (e.g., using a linter like Black).

6. Commit your changes with clear, concise messages. We recommend following the Conventional Commits specification (e.g., feat: added new security check).
```bash
   git commit -m "feat: add new security check"
```

7. Push your branch to your fork on GitHub.
```bash
   git push origin feature/your-awesome-feature 
```

8. Open a Pull Request (PR) targeting the main branch of the original CipherVault repository.

We appreciate clean, well-documented code and will review your PR as quickly as possible!
Thank you for helping improve CipherVault ❤️
