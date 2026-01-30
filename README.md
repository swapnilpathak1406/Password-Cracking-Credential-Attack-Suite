🔐 Password Cracking & Credential Attack Suite (Simulation)
📌 Project Overview

This project is a Password Security Auditing Toolkit developed using Python.
It demonstrates how weak passwords can be identified using dictionary attacks, brute-force simulations, and password strength analysis in a safe and ethical environment.

⚠️ Note:
This project is strictly for educational and ethical purposes.
It does NOT perform real password cracking on live systems.

🎯 Objectives

Understand how passwords are hashed and stored

Simulate dictionary and brute-force password attacks

Analyze password strength using entropy and complexity

Generate a security audit report

Learn defensive password security practices

🛠️ Technologies Used

Programming Language: Python 3

IDE: Visual Studio Code

Libraries Used:

hashlib

itertools

string

math

(No external libraries required)

📂 Project Structure
password_audit_suite/
│
├── main.py
├── dictionary_generator.py
├── brute_force_simulator.py
├── password_strength.py
├── hash_utils.py
├── report_generator.py
└── README.md

⚙️ Module Description
1️⃣ dictionary_generator.py

Generates custom password wordlists

Includes uppercase, lowercase, leetspeak, and numeric variations

2️⃣ hash_utils.py

Creates password hashes using:

MD5

SHA1

SHA256

3️⃣ brute_force_simulator.py

Simulates brute-force attacks

Tries combinations of lowercase letters and digits

Limited length for safety

4️⃣ password_strength.py

Calculates password entropy

Classifies passwords as:

Weak

Moderate

Strong

5️⃣ report_generator.py

Displays a password security audit report

Shows cracked passwords and strength rating

6️⃣ main.py

Main execution file

Integrates all modules

Runs the complete audit workflow

▶️ How to Run the Project
Step 1: Install Python

Download from: https://www.python.org

✔ Make sure “Add Python to PATH” is selected

Step 2: Open Project in VS Code

Open VS Code

File → Open Folder → password_audit_suite

Step 3: Run the Code

Open terminal in VS Code and run:

python main.py

📊 Sample Output
PASSWORD SECURITY AUDIT REPORT

User: user1
Cracked Password: password123
Strength: Weak
--------------------------------
User: user2
Cracked Password: admin
Strength: Weak
--------------------------------

📈 Learning Outcomes

Understand password hashing mechanisms

Learn ethical password auditing techniques

Gain hands-on experience with Python security tools

Understand the importance of strong password policies

🔒 Ethical Disclaimer

This project is intended only for educational purposes.
Do not use this tool on real systems without permission.
Unauthorized password cracking is illegal and unethical.

👨‍💻 Author

Swapnil Govind Pathak
Cybersecurity Student
