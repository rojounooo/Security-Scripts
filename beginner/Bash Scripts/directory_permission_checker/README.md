# 🔐 Permission Checker Script

This Bash script checks the permissions of each directory inside `/home/` and logs whether the permissions are secure (755) or overly permissive.

---

## ⚙️ Description

The script inspects each subdirectory in `/home/` and writes the permission status into a log file named `permission_checker.log`.

---

## ✅ Features

- Checks all directories under `/home/`
- Identifies directories with overly permissive permissions
- Logs results to a file for review

---

## 📌 Requirements

- Linux/Unix-based OS with Bash
- Permissions to read directories in `/home/`

---

## 🚀 How to Run

1. **Make the script executable:**

   ```bash
   chmod +x permission_checker.sh
   ```

2. **Run the script:**

   ```bash
   ./permission_checker.sh
   ```

3. **Review the results:**

   The results are saved in `permission_checker.log`.

---

## 📎 Notes

- This script only checks directories (not files).
- It assumes a typical Linux permission scheme (e.g., 755 = `rwxr-xr-x`).

---

## 📝 License

This script is licensed under the **MIT License**.
