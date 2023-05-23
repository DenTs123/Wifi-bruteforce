import os
import shutil
import patoolib

def extract_and_copy(source_folder, target_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            patoolib.extract_archive(file_path, outdir=target_folder)

source_folder = 'common-password-list'
target_folder = 'passwords'

extract_and_copy(source_folder, target_folder)
