#!/usr/bin/env python3

import os
import re
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from urllib.parse import urljoin
import threading

init(autoreset=True)

# ─────────────────────────────────────────────
# WP PAWN: Python WP PAWN
# Author: Subir Sutradhar
# GitHub: github.com/subir-the-coder/
# ─────────────────────────────────────────────

def banner():
    print(Fore.RED + r"""
██╗    ██╗██████╗     ██████╗  █████╗ ██╔    ██╗███╗   ██╗
██║    ██║██╔══██╗    ██╔══██╗██╔══██╗██║    ██║████╗  ██║
██║ █╗ ██║██████╔╝    ██████╔╝███████║██║ █╗ ██║██╔██╗ ██║
██║███╗██║██╔═══╝     ██╔═══╝ ██╔══██║██║███╗██║██║╚██╗██║
╚███╔███╔╝██║         ██║     ██║  ██║╚███╔███╔╝██║ ╚████║
 ╚══╝╚══╝ ╚═╝         ╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═══╝
           Author: Subir Sutradhar | Coded in Python | v 1.0
    """ + Style.RESET_ALL)

def fetch_url(session, url):
    try:
        res = session.get(url, timeout=10, allow_redirects=True, verify=False)
        return res
    except Exception as e:
        return None

# ──────────────────────────────
# 1. Detect WordPress Version
# ──────────────────────────────

import re

def detect_version(url):
    print(f"{Fore.YELLOW}[+] Detecting WordPress version...{Style.RESET_ALL}")
    paths = ["readme.html", "wp-includes/version.php"])
    session = requests.Session()

    for path in paths:
        full_url = urljoin(url, path)
        try:
            response = session.get(full_url, timeout=10)
            if response.status_code == 200:
                if "readme.html" in path and "wordpress.org" in response.text.lower():
                    print(f"{Fore.GREEN}[+] Possible version info in: {full_url}")
                    # 🔍 Extract version from HTML
                    match = re.search(r'Version\s+([\d.]+)', response.text, re.IGNORECASE)
                    if match:
                        version = match.group(1)
                        print(f"{Fore.CYAN}[+] WordPress Version Detected: {version}{Style.RESET_ALL}")
                    return

                elif "version.php" in path and "wp_version" in response.text:
                    print(f"{Fore.GREEN}[+] Version file found: {full_url}")
                    match = re.search(r"\$wp_version\s*=\s*'([\d.]+)'", response.text)
                    if match:
                        version = match.group(1)
                        print(f"{Fore.CYAN}[+] WordPress Version Detected: {version}{Style.RESET_ALL}")
                    return
        except Exception as e:
            print(f"{Fore.RED}[X] Error detecting version: {e}")

# Remaining functions omitted for brevity in the packaged script. Use the full script in repo.
def main():
    banner()
    url = input(Fore.CYAN + "[~] Enter target WordPress site (e.g., https://example.com): ").strip("/")
    print(Fore.MAGENTA + f"[~] Scanning: {url}\n")

    detect_version(url)
    # detect_plugins(url)
    # detect_themes(url)
    # enumerate_users(url)
    # brute_force_login(url)

if __name__ == "__main__":
    main()
