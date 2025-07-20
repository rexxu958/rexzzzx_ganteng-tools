import socket
import threading

class DDoSModule:
    def __init__(self):
        self.target = ""
        self.port = 0
        self.threads = 5  # Default untuk non-root
        
    def udp_flood(self):
        # Implementasi UDP flood non-root
        pass
        
    def http_flood(self):
        # Implementasi HTTP flood
        pass
        
    def run(self):
        print("[+] Mode DDoS (Non-Root)")
        self.target = input("Target IP/Domain: ")
        self.port = int(input("Port: "))
        
        print("1. UDP Flood")
        print("2. HTTP Flood")
        
        choice = input("Pilih metode: ")
        if choice == "1":
            self.udp_flood()
        elif choice == "2":
            self.http_flood()
