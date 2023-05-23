import os

def merge_files_to_txt(source_folder, target_file):
    with open(target_file, 'w') as outfile:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as infile:
                    outfile.write(infile.read())

source_folder = 'passwords'
target_file = r'C:\Users\acer\OneDrive\Рабочий стол\Wifi bruteforce\Versions\2.0\passwords.txt'

merge_files_to_txt(source_folder, target_file)
