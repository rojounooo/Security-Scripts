
# Compromised Password Checker using Have I Been Pwned API

This Python script checks whether a password has been compromised in known data breaches by querying the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API.

It uses the k-Anonymity model to ensure your password is never sent in plain text.

---

## 🔐 How It Works

1. The password is hashed using SHA-1.
2. Only the **first 5 characters** of the hash are sent to the Have I Been Pwned API.
3. The API responds with all matching suffixes.
4. The script checks if your hash suffix is among them.

This preserves your privacy while still checking against a massive database of breached passwords.

---

## 📦 Requirements

- Python 3.x
- `requests` library

You can install the required library using:

```bash
pip install requests
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Run the script:

```bash
python breach_checker.py
```

3. Enter the password when prompted.

---

## 📊 Output Example

```
Enter a password to check if it has been compromised: password123
Your password has been compromised 1615071 times.
```

---

## 📌 Notes

- The API uses a secure and anonymous method to check passwords.
- This script is for educational or personal use; do not use it for malicious purposes.
- You should never reuse passwords found to be compromised.

---

## 📝 License

This script is licensed under the **MIT License**.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
