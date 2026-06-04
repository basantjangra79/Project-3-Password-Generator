# 🔐 Password Generator

A simple and secure Python-based Password Generator that creates strong random passwords using lowercase letters, uppercase letters, digits, and special characters.

## 📌 Features

- Generate passwords of custom length
- Includes:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Numbers (`0-9`)
  - Special characters (`@#$%&*_-+=!`)
- Guarantees at least:
  - 1 lowercase letter
  - 1 uppercase letter
  - 1 digit
  - 1 special character
- Uses Python's `secrets` module for cryptographically secure password generation
- Option to regenerate passwords without restarting the program
- Handles invalid inputs gracefully

---

## 📂 Project Structure

```text
Project-3-Password-Generator/
│
├── main.py      # Password Generator source code
└── README.md    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Clone the Repository

```bash
git clone https://github.com/basantjangra79/Project-3-Password-Generator.git
cd Project-3-Password-Generator
```

### Run the Program

```bash
python main.py
```

---

## 💻 Example Usage

```text
Welcome to Password Generator!

Enter Password Length: 12

Your Password: A@8mK#2xPq7!

======================================== Coded by: Basant Jangra ========================================

Wants to Re-Generate Password ? [y/n]: y
```

---

## ⚙️ How It Works

1. User enters the desired password length.
2. The program ensures the password contains:
   - One lowercase character
   - One uppercase character
   - One numeric character
   - One special character
3. Remaining characters are randomly selected from all available character sets.
4. The password is shuffled for better randomness.
5. The generated password is displayed to the user.

---

## 🔒 Security

This project uses Python's built-in `secrets` module instead of the `random` module.

Why?

- Designed for cryptographic applications
- Generates unpredictable values
- Suitable for password generation and security-related tasks

---

## 🛠 Technologies Used

- Python 3
- `string` module
- `secrets` module

---

## 📖 Source Code

Repository:

https://github.com/basantjangra79/Project-3-Password-Generator/tree/main

Main program:

```python
main.py
```

---

## 👨‍💻 Author

**Basant Jangra**

GitHub: https://github.com/basantjangra79

---

## 📜 License

This project is open-source and available for learning, educational purposes, and personal use.

⭐ If you found this project useful, consider giving the repository a star.
