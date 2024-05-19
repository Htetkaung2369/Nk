import requests
from bs4 import BeautifulSoup

# Target URL ကို သတ်မှတ်ခြင်း
target_url = "http://example.com"

# စားဝင်ဖွယ်ရှိသော directories များစစ်ဆေးခြင်း
common_dirs = ['admin', 'login', 'dashboard', 'config', 'uploads']

def check_common_directories(url):
    print("[*] Checking for common directories...")
    for directory in common_dirs:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"[+] Found directory: {full_url}")
        else:
            print(f"[-] No directory found at: {full_url}")

def check_sql_injection(url):
    print("[*] Checking for SQL injection...")
    sql_payload = "' OR '1'='1"
    response = requests.get(url + sql_payload)
    if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
        print(f"[+] Potential SQL Injection vulnerability found at: {url}")
    else:
        print(f"[-] No SQL Injection vulnerability found at: {url}")

def main():
    print(f"[*] Starting scan on: {target_url}")
    check_common_directories(target_url)
    check_sql_injection(target_url)
    print("[*] Scan complete.")

if __name__ == "__main__":
    main()
