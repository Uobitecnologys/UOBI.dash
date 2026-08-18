import socket
import time
import os
import sys
import subprocess
import json
import urllib.parse
import urllib.request

# Configuration file for permanent storage
CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "password": "uobi",
    "theme": "Default"
}

# Function to load config permanently
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return DEFAULT_CONFIG.copy()
    else:
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

# Function to save config permanently
def save_config(config_data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")

CONFIG = load_config()

RESET = "\033[0m"
blue = "\033[94m"
cyan = "\033[36m"
red = "\033[91m"
yellow = "\033[93m"
magenta = "\033[95m"
green = "\033[92m"
white = "\033[97m"

def apply_theme():
    global blue, cyan, red, yellow, magenta, green, white
    if CONFIG.get("theme") == "Hacker Green":
        blue = green = cyan = yellow = magenta = white = "\033[92m"
        red = "\033[90m"
    elif CONFIG.get("theme") == "Matrix Red":
        blue = green = cyan = yellow = magenta = white = "\033[91m"
        red = "\033[93m"
    else: 
        blue = "\033[94m"
        cyan = "\033[36m"
        red = "\033[91m"
        yellow = "\033[93m"
        magenta = "\033[95m"
        green = "\033[92m"
        white = "\033[97m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_wikipedia(query):
    print(f"\n[+] Searching for: '{query}'...\n" + "=" * 50)
    encoded_query = urllib.parse.quote(query)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:109.0) Gecko/109.0 Firefox/115.0"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            print(f"Title   : {data.get('title')}")
            print(f"URL     : {data.get('content_urls', {}).get('desktop', {}).get('page')}")
            print(f"\nAnswer  :\n{data.get('extract')}")
            print("=" * 50)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Not Found.")
        else:
            print(f"HTTP Error: {e.code}")
    except Exception as e:
        print(f"Error aaya: {e}")

def play_intro():
    clear_screen()
    try:
        columns = os.get_terminal_size().columns
    except:
        columns = 40
    
    title = "UOBI TECHNOLOGY"
    subtitle = "PRESENTS"
    
    print("\n" * 3)
    padding = " " * max(0, (columns - len(title)) // 2)
    sys.stdout.write(padding + blue)
    for char in title:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write(RESET + "\n\n")
    
    time.sleep(1)
    sub_padding = " " * max(0, (columns - len(subtitle)) // 2)
    print(sub_padding + yellow + subtitle + RESET)
    time.sleep(1)

apply_theme()
play_intro()
clear_screen()

print("System Starting...")

for i in range(1, 101):
    time.sleep(0.04) 
    filled_len = int(30 * i // 100)
    bar = "█" * filled_len + "-" * (30 - filled_len)
    sys.stdout.write(f"\r[{bar}] {i}% ")
    sys.stdout.flush()

print("\n\nEntering...")
time.sleep(1)
clear_screen()

print("=" * 20)
print(f"{blue}Uobi Technology {RESET}")
print("=" * 20)

print(f"{cyan}Software starting...\n")

i = 1
while i <= 10:
    print(f"Installing Required pkg's...({i}/10)")
    time.sleep(0.1)
    i += 1

print(f"{RESET}=" * 30)    
input(f"{red}>>>Pkg's Successfully Installed | >Press Enter<{RESET}")
print(f"{RESET}=" * 30)

clear_screen()
password = input(f"{yellow}Enter Passwordn(Default Passwrd 'uobi') : ")
if password == CONFIG["password"]:
    print(f"{green}Login successfully..{RESET}")
    print(f"{yellow} Welcome Back  ")
    time.sleep(1)
else:
    print(f"{red}Access Blocked! Incorrect Password.{RESET}")
    sys.exit()

while True:
    apply_theme()
    clear_screen()
    print(f"{blue}Uobi Technology {RESET}")
    print("=" * 25)
    print(f"{yellow}System Active{RESET}")
    print("=" * 25)
    
    print(f"{magenta}1.  Port Scan")
    print("2. Watch Time (Clock)")
    print("3. Domain IP Finder")
    print("4. Notebook ")
    print("5. Terminal Shell")
    print("6. System Exit")
    print("7. Search")
    print("8. Settings")
    print(f"9. Credits{RESET}")
    
    print("=" * 25)
    
    action = input(f"{green}Choose Option (1-9) : ")
    print(f"{RESET}=" * 25)
    
    if action == "1":
        print(f"{yellow}Port Scanning Started{RESET}")
        print("=" * 20)
        target = input(f"{red}Enter Target IP/Domain : ").strip()
        target = target.replace("https://", "").replace("http://", "").split("/")[0]
        
        ports_input = input(f"Enter Ports (e.g. 80,443,22 or 20-80) : ").strip()
        
        # FIXED: Port Parsing logic
        port_list = []
        try:
            if "-" in ports_input:
                start_p, end_p = map(int, ports_input.split("-"))
                port_list = list(range(start_p, end_p + 1))
            elif "," in ports_input:
                port_list = [int(p.strip()) for p in ports_input.split(",") if p.strip().isdigit()]
            else:
                port_list = [int(ports_input)]
        except ValueError:
            print(f"{red}Invalid Port Input! Scanning default ports (80, 443)...{RESET}")
            port_list = [80, 443]

        try:
            target_ip = socket.gethostbyname(target)
            print(f"{cyan}Scanning Target: {target} ({target_ip}){RESET}\n")
            
            for port in port_list:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))
                
                if result == 0:
                    print(f"{green}Port :{port:5} Open{RESET}")
                else:
                    print(f"{red}Port :{port:5} Closed{RESET}")
                s.close()
        except Exception as e:
            print(f"{red}Error found: {e}{RESET}")
            
        input(f"\n{blue}Press Enter to go back to Main Menu...{RESET}")

    elif action == "2":
        print("=" * 25)
        print(f"{yellow}      Live Clock {RESET}")
        print("=" * 25)
        try:
            while True:
                current_time = time.strftime("%H:%M:%S %p")
                current_date = time.strftime("%Y-%m-%d")
                print(f"{red}Date: {current_date} | Time: {current_time}{RESET}", end="\r")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{yellow}Clock stopped. Returning to menu...{RESET}")
            time.sleep(1)

    elif action == "3":
        domain = input(f"{yellow}Enter Domain Name (e.g., google.com): ")
        domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
        try:
            ip_address = socket.gethostbyname(domain)
            print("=" * 20)
            print(f"{cyan}Domain : {domain}")
            print(f"{green}IP Address: {ip_address}{RESET}")
            print("=" * 20)
        except socket.gaierror:
            print(f"{red}\nInvalid Domain or Network Error!{RESET}")
            
        input(f"\n{blue}Press Enter to go back to Main Menu...{RESET}")

    elif action == "4":
        clear_screen()
        print("=" * 30)
        print(f"{yellow}      NOTEBOOK {RESET}")
        print("=" * 30)
        print(f"{magenta}1. Create New Note & Save")
        print(f"2. Read Saved Notes{RESET}")
        print("=" * 30)
        
        note_option = input(f"{green}Choose Option (1-2) : ")
        
        if note_option == "1":
            file_name = input(f"\n{cyan}Enter File Name (e.g., my_note): ").strip()
            if not file_name.endswith(".txt"):
                file_name += ".txt"
                
            print(f"{RESET}=" * 20)
            note = input(f"{yellow}Enter Your Text : ")
            print(f"{RESET}=" * 20)
            
            save = input("\nSAVE File (Press Enter to Save): ")
            if save == "":
                try:
                    with open(file_name, "w") as f:
                        f.write(note)
                    print("=" * 30)
                    print(f"{green}File '{file_name}' Successfully Saved to Device!{RESET}")
                    print("=" * 30)
                except Exception as e:
                    print(f"{red}Failed to save file: {e}{RESET}")
            else:
                print("=" * 20)
                print(f"{red}\nFile Not Saved!!{RESET}")
                print("=" * 20)
                
        elif note_option == "2":
            clear_screen()
            print(f"{cyan}Saved Notes in Current Directory:{RESET}")
            print("=" * 30)
            
            txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
            
            if txt_files:
                for idx, fname in enumerate(txt_files, 1):
                    print(f"{yellow}{idx}. {fname}{RESET}")
                print("=" * 30)
                
                open_file = input(f"\n{green}Enter File Name to Open: ").strip()
                if not open_file.endswith(".txt"):
                    open_file += ".txt"
                    
                if os.path.exists(open_file):
                    print(f"{RESET}=" * 30)
                    print(f"{yellow}--- Content of {open_file} ---{RESET}")
                    with open(open_file, "r") as f:
                        print(f"{white}{f.read()}")
                    print(f"{RESET}=" * 30)
                else:
                    print(f"{red}\nFile not found!{RESET}")
            else:
                print(f"{red}No saved .txt notes found in this directory.{RESET}")

        input(f"\n{blue}Press Enter For Go Back to Main Menu...{RESET}")

    elif action == "5":
        clear_screen()
        print(f"{green}=== TERMINAL ==={RESET}")
        print(f"{yellow}Type 'exit' or 'back' to return to Main Menu{RESET}\n")
        
        while True:
            current_path = os.getcwd()
            cmd = input(f"{cyan}{current_path} $ ").strip()
            
            if cmd.lower() in ["exit", "back"]:
                print(f"{yellow}Returning to Main Menu...{RESET}")
                time.sleep(1)
                break
            
            if cmd == "":
                continue
                
            if cmd.startswith("cd"):
                parts = cmd.split(maxsplit=1)
                if len(parts) > 1:
                    target_dir = parts[1]
                    try:
                        os.chdir(target_dir)
                    except FileNotFoundError:
                        print(f"{red}No such file or directory: {target_dir}{RESET}")
                    except Exception as e:
                        print(f"{red}Error: {e}{RESET}")
                else:
                    os.chdir(os.path.expanduser("~"))
            else:
                try:
                    os.system(cmd)
                except Exception as e:
                    print(f"{red}Command execution error: {e}{RESET}")

    elif action == "6":
        clear_screen()
        sys.exit()

    elif action == "7":
        clear_screen()
        user_input = input(f"{yellow}Search : ")
        if user_input.strip():
            search_wikipedia(user_input)
        input(f"\n{blue}Press Enter to go back to Main Menu...{RESET}")

    elif action == "8":
        while True:
            clear_screen()
            print("=" * 25)
            print(f"{yellow}     SETTINGS MENU      {RESET}")
            print("=" * 25)
            print(f"{magenta}1. Change Password")
            print(f"2. Change Color Theme [{CONFIG['theme']}]")
            print("3. Reset to Default Password & Settings")
            print(f"4. Back to Main Menu{RESET}")
            print("=" * 25)
            
            set_choice = input(f"{green}Choose Option (1-4) : {RESET}").strip()
            
            if set_choice == "1":
                old_p = input(f"\n{yellow}Enter Current Password (Default Passwrd 'uobi' : {RESET}")
                if old_p == CONFIG["password"]:
                    new_p = input(f"{cyan}Enter New Password: {RESET}").strip()
                    if new_p:
                        # FIXED: Save password permanently to JSON
                        CONFIG["password"] = new_p
                        save_config(CONFIG)
                        print(f"\n{green}Password change{RESET}")
                    else:
                        print(f"\n{red}Password cannot be empty!{RESET}")
                else:
                    print(f"\n{red}Incorrect current password!{RESET}")
                time.sleep(1.5)

            elif set_choice == "2":
                print("\nChoose Color Theme:")
                print("1. Default (Multi-Color)")
                print("2. Hacker Green")
                print("3. Matrix Red")
                th = input("Choice (1-3): ").strip()
                if th == "2": CONFIG["theme"] = "Hacker Green"
                elif th == "3": CONFIG["theme"] = "Matrix Red"
                else: CONFIG["theme"] = "Default"
                
                # FIXED: Save theme permanently
                save_config(CONFIG)
                apply_theme()
                print(f"\n{green}Theme applied & saved successfully!{RESET}")
                time.sleep(1)

            elif set_choice == "3":
                CONFIG = DEFAULT_CONFIG.copy()
                save_config(CONFIG)
                apply_theme()
                print(f"\n{green}Password and Settings reset to default!{RESET}")
                time.sleep(1.5)

            elif set_choice == "4":
                break

    elif action == "9":
        clear_screen()
        print("=" * 35)
        print(f"{cyan}       DEVELOPER CREDITS         {RESET}")
        print("=" * 35)
        print(f"{yellow} Created By   : Uobi Technology{RESET}")
        print(f"{green} Lead Dev     : Ubaid{RESET}")
        print(f"{magenta} Version      : 0.13.0{RESET}")
        print(f"{white} Description  : All-in-one CLI Tool{RESET}")
        print("=" * 35)
        input(f"\n{blue}Press Enter to go back to Main Menu...{RESET}")
