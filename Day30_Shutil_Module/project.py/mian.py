import os
import shutil


# -------------------------------
# 1. Copy File
# -------------------------------
def copy_file():
    src = input("Enter source file path: ")
    dst = input("Enter destination file path: ")

    if not os.path.isfile(src):
        print("Error: Source file not found.")
        return

    try:
        shutil.copy2(src, dst)
        print("File copied successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 2. Copy Folder
# -------------------------------
def copy_folder():
    src = input("Enter source folder path: ")
    dst = input("Enter destination folder path: ")

    if not os.path.isdir(src):
        print("Error: Source folder not found.")
        return

    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print("Folder copied successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 3. Move File
# -------------------------------
def move_file():
    src = input("Enter source file path: ")
    dst = input("Enter destination path: ")

    if not os.path.exists(src):
        print("Error: File not found.")
        return

    try:
        shutil.move(src, dst)
        print("File moved successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 4. Rename File
# -------------------------------
def rename_file():
    old_name = input("Enter current file path: ")
    new_name = input("Enter new file path: ")

    if not os.path.exists(old_name):
        print("Error: File not found.")
        return

    try:
        os.rename(old_name, new_name)
        print("File renamed successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 5. Create ZIP Backup
# -------------------------------
def create_zip_backup():
    folder = input("Enter folder path to backup: ")

    if not os.path.isdir(folder):
        print("Error: Folder not found.")
        return

    zip_name = input("Enter backup name: ")

    try:
        shutil.make_archive(zip_name, "zip", folder)
        print("ZIP backup created successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 6. Extract ZIP Backup
# -------------------------------
def extract_zip():
    zip_file = input("Enter ZIP file path: ")
    destination = input("Enter extraction folder: ")

    if not os.path.isfile(zip_file):
        print("Error: ZIP file not found.")
        return

    try:
        shutil.unpack_archive(zip_file, destination)
        print("ZIP extracted successfully.")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# 7. Check Disk Usage
# -------------------------------
def check_disk_usage():
    path = input("Enter path: ")

    try:
        total, used, free = shutil.disk_usage(path)

        print("\nDisk Usage")
        print(f"Total Space : {total // (1024**3)} GB")
        print(f"Used Space  : {used // (1024**3)} GB")
        print(f"Free Space  : {free // (1024**3)} GB")

    except Exception as e:
        print("Error:", e)


# -------------------------------
# 8. Find Python Executable
# -------------------------------
def find_python():
    python_path = shutil.which("python")

    if python_path:
        print("Python found at:")
        print(python_path)
    else:
        print("Python executable not found.")


# -------------------------------
# Main Menu
# -------------------------------
def main():

    while True:

        print("\n=====================================")
        print("      SMART FILE BACKUP MANAGER")
        print("=====================================")

        print("1. Copy File")
        print("2. Copy Folder")
        print("3. Move File")
        print("4. Rename File")
        print("5. Create ZIP Backup")
        print("6. Extract ZIP Backup")
        print("7. Check Disk Usage")
        print("8. Find Python Executable")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            copy_file()

        elif choice == "2":
            copy_folder()

        elif choice == "3":
            move_file()

        elif choice == "4":
            rename_file()

        elif choice == "5":
            create_zip_backup()

        elif choice == "6":
            extract_zip()

        elif choice == "7":
            check_disk_usage()

        elif choice == "8":
            find_python()

        elif choice == "9":
            print("Thank you for using Smart File Backup Manager.")
            break

        else:
            print("Invalid Choice. Try Again.")


main()