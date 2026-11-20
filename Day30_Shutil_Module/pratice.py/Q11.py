# Q11. Safe Temporary Folder Cleaner

# Concept: shutil.rmtree(), os.path

# Requirements:

    # Create a dedicated temporary practice folder.
    # Add dummy files and subfolders.
    # Check whether the folder exists.
    # Delete only that test folder.
    # Verify that it has been deleted.

# Steps to Solve:

    # Create a folder named test_delete_folder.
    # Add sample files and a subfolder.
    # Verify that the target path is exactly the test folder.
    # Check whether the folder exists.
    # Use shutil.rmtree() only on this test folder.
    # Verify that the folder no longer exists.
    # Never use this practice program on important directories.


#_-------------------------------------------------------------------------------------------------------------------


import os
import shutil

# Step 1: Create test folder
folder_name = "test_delete_folder"
os.makedirs(folder_name, exist_ok=True)

# Step 2: Create a dummy file
with open(os.path.join(folder_name, "sample.txt"), "w") as file:
    file.write("This is a test file.")

# Step 3: Create a subfolder
os.makedirs(os.path.join(folder_name, "subfolder"), exist_ok=True)

print("Test folder created.")

# Step 4: Check whether folder exists
if os.path.exists(folder_name):
    print("Folder exists.")

    # Step 5: Safety check
    if folder_name == "test_delete_folder":
        shutil.rmtree(folder_name)
        print("Folder deleted successfully.")
    else:
        print("Unsafe folder name. Deletion cancelled.")

# Step 6: Verify deletion
if not os.path.exists(folder_name):
    print("Verification successful: Folder has been removed.")
else:
    print("Folder still exists.")