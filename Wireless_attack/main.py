import os
import time
import platform
import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define color constants
red = Fore.RED
reset = Style.RESET_ALL


def logo():
    logo_text = """\n\n
    __        __ _____ _____ _____     _____  _______  _____   _______ _    _ 
    \ \      / // ____/ ____|  __ \   |  __ \|__   __|/ ____| |__   __| |  | |
     \ \    / /| |   | |    | |__) |  | |__) |  | |  | (___      | |  | |__| |
      \ \  / / | |   | |    |  _  /   |  ___/   | |   \___ \     | |  |  __  |
       \ \/ /  | |___| |____| | \ \   | |       | |   ____) |    | |  | |  | |
        \__/    \_____\_____|_|  \_\  |_|       |_|  |_____/     |_|  |_|  |_|
    """
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the logo line by line with a delay
    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)

    # Print additional info
    print(Style.BRIGHT + '  by Dandelion        v0.1    Made in Ukraine :)' + reset)
    time.sleep(2)


def wifi_scan():
    os_system = platform.system()
    if os_system == "Linux":
        command = ["sudo", "iwlist", "scan"]
    else:
        print(red + f"Wi-Fi scanning not implemented for {os_system}" + reset)
        time.sleep(2)
        return

    print(f"Running command: {' '.join(command)}")

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"Command output:\n{result.stdout}")
        if result.returncode != 0:
            print(red + f"Error executing command: {result.stderr}" + reset)
    except Exception as e:
        print(red + f"Error running command: {e}" + reset)


def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
 __  __ ______ _   _ _    _ 
|  \/  |  ____| \ | | |  | |
| \  / | |__  |  \| | |  | |
| |\/| |  __| | . ` | |  | |
| |  | | |____| |\  | |__| |
|_|  |_|______|_| \_|\____/ 
        ''')
        print('I think, if you download this util, you are ready)\n 1) Wifi Scan')
        print('0) ! EXIT !')
        try:
            home_page = int(input('\n [+] Choose your choice: '))
        except ValueError:
            print(red + 'Print real point of menu!' + reset)
            time.sleep(2)
            continue

        if home_page == 0:
            break
        elif home_page == 1:
            wifi_scan()
        else:
            print(red + 'Print real point of menu!' + reset)
            time.sleep(2)


if __name__ == '__main__':
    logo()
    menu()
