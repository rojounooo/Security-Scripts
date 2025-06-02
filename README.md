# 🔐 Security Scripts Collection

This repository contains a curated set of beginner to advanced security scripts written for educational and professional use. These scripts demonstrate key cybersecurity concepts across areas such as system hardening, intrusion detection, password auditing, and more.

---

## 📂 Repository Structure

- `beginner/` - Foundational scripts for learning basic security concepts.
- `intermediate/` - Scripts that involve automation, scanning, and log analysis.
- `advanced/` - Projects that simulate real-world scenarios like intrusion detection or C2 frameworks.

---

## 📊 Script Overview

| Level       | Script Name                | Description                       | Language | Status |
|-------------|----------------------------|-----------------------------------|----------|--------|
| Beginner    | [password_checker.py](beginner/Python Scripts/password_strength_checker/)| Takes a password and compares to a password policy checklist|Python|Complete|
| Beginner    | [breach_checker.py](beginner/Python Scripts/password_breach_checker/)| Takes a password, hashes it and then makes a request to HaveIBeenPwned |Python|Complete|
| Beginner    | [simple_nmap_scanner.py](beginner/Python Scripts/simple_port_scanner/)| Takes an host IP or URL and attempts to enumerate every port |Python|Complete|
| Beginner    | [file_integrity_monitor.py](beginner\Python Scripts\simple_port_scanner/)| Monitors files or directories for unauthorized changes |Python|Complete|
| Beginner    | [permission_checker.sh](beginner/Bash Scripts/directory_permission_checker/)| Checks if directories under /home are globally accessible |Bash|Complete|

---

## 📌 Usage

Each script is documented inside its respective folder. To run a script e.g. password_checker.py:

```bash
cd beginner/Python Scripts/password_strength_checker
python3 password_checker.py
```
# ⚠️ DISCLAIMER

This repository is intended **solely for educational, ethical, and authorized testing purposes**. The scripts, tools, and techniques provided are designed to help security professionals, students, and researchers understand and improve cybersecurity practices.

## ❗ You MUST agree to the following:

- You will **not** use any script, tool, or method found in this repository to compromise, damage, or interfere with systems or networks you do not own or have **explicit written permission** to test.
- You understand that using these tools irresponsibly or illegally could violate local, national, or international laws, and you are solely responsible for your actions.
- The authors, contributors, and maintainers of this repository are **not liable** for any misuse or damage resulting from the use of the content within.

## ✅ Responsible Use Examples:

- Practicing in a home lab or virtual environment you control.
- Using on systems where you have **permission to test** (e.g., bug bounty programs, CTFs).
- Educational or research use under supervision or within guidelines.

---

> **Use responsibly. Hack ethically. Learn continuously.**

