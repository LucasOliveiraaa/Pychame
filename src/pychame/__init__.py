from os.path import exists, join
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()

CERT_PATH = (CURRENT_DIR / "keys" / "cert.pem")
KEY_PATH = (CURRENT_DIR / "keys" / "key.pem")
INDEX_PATH = (CURRENT_DIR / "page" / "index.html")

def main():
    if not exists(CERT_PATH):
        print("ERROR: Cert not found, reinstall the pychame to fix it")
        print(f"Cert Path: {CERT_PATH}")
        exit(0)

    if not exists(KEY_PATH):
        print("ERROR: Key not found, reinstall the pychame to fix it")
        print(f"Key Path: {KEY_PATH}")
        exit(0)
    
    if not exists(INDEX_PATH):
        print("ERROR: Index HTML not found, reinstall the pychame to fix it")
        print(f"Index HTML Path: {INDEX_PATH}")
        exit(0)