import os
import time
from _ast import For

from colorama import init, Fore, Style

import systemFiles.wifi_attack as sd

init()

red = For.RED
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
    os.system('cls' if os.name == 'nt' else 'clear')

    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)

    print(Style.BRIGHT + '  by Dandelion        v0.1    Made in Ukraine :)' +reset)
    time.sleep(2)

def menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
 __  __ ______ _   _ _    _ 
|  \/  |  ____| \ | | |  | |
| \  / | |__  |  \| | |  | |
| |\/| |  __| | . ` | |  | |
| |  | | |____| |\  | |__| |
|_|  |_|______|_| \_|\____/ ''')
            print('I think? if you download this util? you are ready)\n 1) Wifi Hack')
            print('0) ! EXIT !')
            home_page = int(input('\n [+] Chose your choice: '))

            if home_page == 0:
                break
            elif home_page == 1:
                sd.scan_wifi_networks()
            else:
                print(red + 'Print real point of menu!' + reset)

if __name__ == '__main__':
    logo()
    menu()
