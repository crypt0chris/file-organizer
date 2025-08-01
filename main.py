import os
import shutil

def organize(folder):
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(folder, filename), os.path.join(ext_folder, filename))

if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize(path)
