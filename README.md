# Automated Mimikatz Credential Extraction (`mimikatz_final.py`)

## 📌 Project Overview

This repository contains a Python automation script developed for a simulated Active Directory penetration testing assessment for **XYZ Corp**. The primary objective is to test and validate Windows security controls against memory-based credential dumping techniques in a controlled lab environment.

The script automates binary verification, command execution via `subprocess`, and log output capturing to streamline security audits and compliance reporting.

---

## 🛠️ Features

* **Path Verification:** Validates the presence of the Mimikatz executable using `os.path.exists` prior to execution.
* **Automated Command Execution:** Runs specified Mimikatz commands (e.g., privilege escalation, LSASS dumping) via Python subprocesses.
* **Structured Audit Logging:** Automatically outputs standard execution logs to `mimikatz_log.txt` for record-keeping and post-test analysis.
* **Error Handling:** Captures execution errors cleanly to prevent unhandled runtime exceptions.

---

## 📋 System Requirements & Environment

* **Operating System:** Windows 10 / Windows Server (Lab Environment)
* **Interpreter:** Python 3.x
* **Standard Modules:** `os`, `subprocess`, `datetime`
* **Tools:** `mimikatz.exe` (Must be located in the script directory or target path)

---

## 🚀 Getting Started

### 1. File Setup
Ensure the script file is named **`mimikatz_final.py`** (required for automated CodeGrade scoring):

```bash
mv mimikatz_starter.py mimikatz_final.py
