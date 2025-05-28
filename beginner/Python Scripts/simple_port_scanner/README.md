# 🔍 Simple Python Port Scanner using Nmap

This Python script scans a target host for open ports using the `nmap` library.

It utilizes the `nmap` tool installed on your system to perform a comprehensive scan across all 65535 TCP ports.

---

## 🛠 How It Works

1. Takes a single command-line argument: the target IP address or hostname.
2. Uses Python's `nmap` module to invoke the `nmap` command.
3. Scans all ports (`1-65535`) on the specified host.
4. Prints out open ports and their states for each protocol.

---

## 📦 Requirements

- Python 3.x
- [`python-nmap`](https://pypi.org/project/python-nmap/) module
- `nmap` must be installed on your system

Install the required Python module using:

```bash
pip install python-nmap
```

Ensure `nmap` is installed on your system:

- On Debian/Ubuntu:
  ```bash
  sudo apt install nmap
  ```

- On macOS (with Homebrew):
  ```bash
  brew install nmap
  ```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Run the script with a target IP or hostname:

```bash
python3 port_scanner.py <host>
```

Example:

```bash
python3 port_scanner.py 192.168.1.1
```

---

## 📊 Output Example

```
Scanning host: 192.168.1.1
Protocol: tcp
Port: 22	State: open
Port: 80	State: open
Port: 443	State: closed
```

---

## ⚠️ Notes

- This tool is for **educational and authorized security testing only**.
- Unauthorized port scanning may violate network policies or laws.
- Always get permission before scanning systems you do not own.

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
