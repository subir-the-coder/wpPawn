# WP PAWN — WordPress Passive & Active Weapon (WP PAWN)

**WP PAWN** is a lightweight Python tool to enumerate WordPress sites and gather reconnaissance data quickly.  
It combines passive checks (version detection, author enumeration) and active checks (plugin/theme discovery, basic brute-force login attempts) with multithreaded probing for speed.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/5a41267a-086e-4156-952c-749b77ecd405" />


> ⚠️ **Important:** This tool is intended for **ethical security testing only**. Do not use it against systems you do not own or do not have explicit permission to test.

---

## Quick facts

- **Script name:** `wp_pawn.py` (or whichever filename you choose)
- **Author:** Subir Sutradhar
- **Version:** v1.0
- **Language:** Python 3.x
- **License:** Apache License 2.0 (see `LICENSE`)

---

## Features

- Detect WordPress version (via `readme.html` and `wp-includes/version.php`)
- Detect common plugins and themes (multithreaded)
- Enumerate author usernames via `/?author=N` redirects
- Basic brute-force login attempts using `data/users.txt` and `data/passwords.txt`
- Fast HTTP requests with session reuse and threading
- Colored terminal output for clear, readable results (via `colorama`)

---

## Requirements

- Python 3.8+ recommended

Install required Python packages:

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**
```
requests
beautifulsoup4
tqdm
colorama
```

**Note:** The script disables SSL verification for some requests (`verify=False`) — this is intentional for recon on misconfigured hosts, but be aware of the implications.

---

## Setup

1. Clone or add the script to your repo.
2. Create a `data/` directory and provide these files (example lists are required for some features):

```
data/
├── themes.txt         # theme names (one per line) OR the script will use default list
├── users.txt          # usernames for brute-force (one per line)
└── passwords.txt      # passwords for brute-force (one per line)
```

3. (Optional) Set up a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

Run the script and follow the prompts:

```bash
python wp_pawn.py
```

Example interactive flow:

1. Enter the target WordPress URL when prompted (e.g. `https://example.com`).
2. The script will:
   - Attempt to detect WordPress version
   - Probe for common plugins (multithreaded)
   - Probe for themes (multithreaded, using `data/themes.txt` if present)
   - Attempt author enumeration
   - Attempt basic brute-force login (if `data/users.txt` and `data/passwords.txt` exist)

---

## Output

- Results are printed to the terminal with color-coded messages:
  - Green = positive detections / success
  - Yellow = informational / progress
  - Red = errors / failures
- You can redirect stdout to a file to save results, e.g.:

```bash
python wp_pawn.py | tee wp_pawn_results.txt
```

---

## Recommended usage & safety

- Only scan WordPress sites you own or have explicit written permission to test.
- Brute-force login functionality can trigger WAFs, lock accounts, or be considered abusive — use responsibly.
- Consider rate-limiting and adding random delays if you integrate this into larger automation.
- For safer testing, use staging environments or intentionally vulnerable test sites.

---

## Extending the tool

Suggested improvements you might add:

- Add CLI flags (`argparse`) for non-interactive batch mode
- Add configurable thread pool size / rate-limit controls
- Add output formats (JSON / CSV) and timestamped result files
- Add optional integration with external APIs (WPScan DB, threat intel)
- Improve brute-force to respect lockout policies and provide a safe mode

---

## Legal

Using this tool without authorization may be illegal. The author provides this tool for educational and authorized security testing only.

---

## Author

**Subir Sutradhar**  
GitHub: https://github.com/subir-the-coder  
Email: subir-the-coder@outlook.com

---

## License

This project is licensed under the Apache License 2.0 — see the `LICENSE` file for details.
