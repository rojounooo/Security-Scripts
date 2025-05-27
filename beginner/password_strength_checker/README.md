
# Password Strength Checker

This Python script evaluates the strength of a password based on a defined policy. It checks for minimum length, presence of uppercase and lowercase letters, digits, and special characters. The script outputs a summary of the password’s compliance with each rule and assigns an overall strength rating.

---

## 🔐 Password Policy

The password must satisfy the following conditions:

- **Minimum length:** 10 characters  
- **At least one uppercase letter:** A–Z  
- **At least one lowercase letter:** a–z  
- **At least one digit:** 0–9  
- **At least one special character:** `@`, `#`, `$`, `%`, `^`, `&`, `+`, `=`, `.`, `_`, `-`

---

## 📦 Requirements

- Python 3.x (No external libraries required)

---

## 🚀 How to Run

1. **Clone or download this repository.**

2. **Run the script:**

   ```bash
   python password_checker.py
   ```

3. **Follow the prompt and enter a password to check its strength.**

---

## 📊 Output Example

```
Password Policy:
- At least 10 characters long
- Contains at least one uppercase letter (A–Z)
- Contains at least one lowercase letter (a–z)
- Contains at least one digit (0–9)
- Contains at least one special character: @ # $ % ^ & + = . _ -

Enter a password to check its strength: P@ssw0rd123

Password Strength Check Results:
Length (≥10 chars):        ✅
Uppercase letters:         ✅
Lowercase letters:         ✅
Digits:                    ✅
Special characters:        ✅

Password Strength: Very Strong
```

---

## 📌 Notes

- If any criteria are not met, the script will highlight it and encourage the user to improve the password.
- This script is a basic checker and does not calculate password entropy.
- It does not check against known breached password databases.

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
