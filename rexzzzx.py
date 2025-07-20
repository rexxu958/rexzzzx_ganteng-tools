#!/usr/bin/env python3
import os
import sys
from modules.ddos import DDoSModule
from modules.osint import OSINTModule
from modules.deface import DefaceModule

class RexzzzxCrasherV3:
    def __init__(self):
        self.version = "2.0"
        self.author = "rexxu958"
        
    def show_banner(self):
        print(f"""
        ██████╗ ███████╗██╗  ██╗███████╗███████╗██╗  ██╗
        ██╔══██╗██╔════╝╚██╗██╔╝╚════██║╚════██║╚██╗██╔╝
        ██████╔╝█████╗   ╚███╔╝  █████╔╝ █████╔╝ ╚███╔╝ 
        ██╔══██╗██╔══╝   ██╔██╗ ██╔═══╝  ╚═══██╗ ██╔██╗ 
        ██║  ██║███████╗██╔╝ ██╗███████╗██████╔╝██╔╝ ██╗
        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝
        Version: {self.version} | By: {self.author}
        """)

    def run(self):
        self.show_banner()
        print("1. DDoS Tools")
        print("2. OSINT Tools")
        print("3. Auto-Deface")
        
        choice = input("Pilih menu: ")
        if choice == "1":
            DDoSModule().run()
        elif choice == "2":
            OSINTModule().run()
        elif choice == "3":
            DefaceModule().run()

if __name__ == "__main__":
    try:
        RexzzzxCrasherV2().run()
    except KeyboardInterrupt:
        print("\n[!] Dihentikan pengguna")
