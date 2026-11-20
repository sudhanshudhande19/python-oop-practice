<p align="center">
  <img src="banner.svg" alt="Day 30 - Shutil Module in Python" width="100%">
</p>

 
# 🐍 Day 30 — Shutil Module in Python

> **Learn → Understand → Practice → Build → Debug → Push**

## 🎯 Learning Objectives

By completing Day 30, I will be able to:

- Understand Python's `shutil` module.
- Copy files and folders.
- Understand the difference between `copy()`, `copy2()`, and `copyfile()`.
- Move and rename files.
- Copy complete directory structures.
- Delete directories safely.
- Check disk usage.
- Find executable programs.
- Create and extract archive files.
- Build a practical File Backup & Organizer Utility.

---


# 📘 Day 30 Theory — Shutil Module in Python

## 1. What is the `shutil` Module?

`shutil` is a built-in Python module used to manage files and folders. It provides ready-made functions to **copy, move, rename, delete, archive, and extract** files and directories.

**Easy definition:** `shutil` is like a file manager inside Python. Instead of doing file operations manually, we can use its functions.

```python
import shutil
```

**Real-life example:** Imagine you want to copy your college notes into a backup folder. Python's `shutil` module can do that with just one function.

## 2. Why Do We Use `shutil`?

- To make backup copies of important files.
- To copy complete folders with their subfolders.
- To move or rename files.
- To create ZIP backups and extract archives.
- To check disk space and locate executable programs.

## 3. Important `shutil` Functions — Easy Meaning

| Function | Simple meaning | Remember it as |
|---|---|---|
| `shutil.copy()` | Copies file data and permission mode | Copy a file |
| `shutil.copy2()` | Copies a file and tries to preserve extra metadata | Copy with details |
| `shutil.copyfile()` | Copies only file contents | Content only |
| `shutil.copytree()` | Copies a complete folder and its contents | Copy a tree |
| `shutil.move()` | Moves or renames a file/folder | Move it |
| `shutil.rmtree()` | Deletes a folder and everything inside it | Remove tree |
| `shutil.which()` | Finds an executable program's path | Find program |
| `shutil.disk_usage()` | Shows total, used, and free disk space | Check storage |
| `shutil.make_archive()` | Creates an archive such as ZIP | Pack files |
| `shutil.unpack_archive()` | Extracts an archive | Unpack files |

## 4. Understand the Difference: `copy()`, `copy2()`, and `copyfile()`

- **`copy()`** copies the file contents and permission mode.
- **`copy2()`** does the same and also attempts to preserve additional metadata, such as modification time.
- **`copyfile()`** copies only the file contents; it does not copy permission mode or other metadata.

**Memory trick:** `copy2` = copy + extra details; `copyfile` = file contents only.

## 5. Copying a Complete Folder

A folder can contain files and other folders. `copytree()` copies the complete directory structure.

```python
import shutil

shutil.copytree("my_notes", "my_notes_backup")
```

Here, `my_notes` is the source and `my_notes_backup` is the new copy. By default, the destination must not already exist.

## 6. Moving and Renaming

`move()` transfers a file or folder to another location. If you give it a new name in the same folder, it can rename the item too.

```python
import shutil

shutil.move("old.txt", "new.txt")  # Rename
shutil.move("report.txt", "backup/report.txt")  # Move
```

**Remember:** Copy makes another copy; move changes the item's location.

## 7. Deleting a Folder Safely

`rmtree()` deletes a folder and all its contents. This is a destructive operation.

```python
import shutil

shutil.rmtree("test_delete_folder")
```

**Safety rule:** Practice only on a folder created for testing. Check the exact path before deletion. Never test with system folders, your home folder, or important project folders.

## 8. Finding Programs and Checking Storage

```python
import shutil

python_path = shutil.which("python")
print(python_path)  # Path, or None if not found

usage = shutil.disk_usage(".")
print("Total:", usage.total)
print("Used:", usage.used)
print("Free:", usage.free)
```

`disk_usage()` returns total, used, and free space in **bytes**. `which()` searches the system's executable search path.

## 9. Creating and Extracting ZIP Archives

```python
import shutil

shutil.make_archive("my_backup", "zip", "my_folder")
shutil.unpack_archive("my_backup.zip", "restored_folder")
```

- `make_archive()` packs a folder into an archive.
- `unpack_archive()` extracts an archive into a folder.

## 10. Quick Revision — Remember in One Minute

- `copy` = copy a file.
- `copy2` = copy a file with extra metadata where supported.
- `copyfile` = copy only contents.
- `copytree` = copy a whole folder.
- `move` = move or rename.
- `rmtree` = delete a whole folder tree — use carefully.
- `which` = find a program.
- `disk_usage` = check storage.
- `make_archive` = create ZIP/archive.
- `unpack_archive` = extract archive.

> **One-line summary:** `shutil` helps Python perform high-level file and folder operations such as copying, moving, deleting, backing up, and archiving.

---

# 1. Introduction to Shutil Module

Python provides a built-in module called `shutil`.

`shutil` stands for **Shell Utilities**. It provides high-level operations for working with files and directories.

### Import Shutil

```python
import shutil
```

### Important Functions

| Function | Description |
|---|---|
| `shutil.copy()` | Copies a file and its permission mode |
| `shutil.copy2()` | Copies a file and attempts to preserve metadata |
| `shutil.copyfile()` | Copies file contents |
| `shutil.copytree()` | Copies an entire directory tree |
| `shutil.move()` | Moves a file or directory |
| `shutil.rmtree()` | Deletes a directory tree |
| `shutil.which()` | Finds the location of an executable |
| `shutil.disk_usage()` | Returns disk usage information |
| `shutil.make_archive()` | Creates an archive file |
| `shutil.unpack_archive()` | Extracts an archive file |

---

# 2. Copying Files

## A. `shutil.copy()`

Copies a file to another location.

```python
import shutil

shutil.copy("source.txt", "backup.txt")
```

Here:
- `source.txt` is the original file.
- `backup.txt` is the copied file.
- The copied file receives the source file's permission mode.

## B. `shutil.copy2()`

Copies a file and attempts to preserve its metadata, such as modification time.

```python
import shutil

shutil.copy2("source.txt", "backup.txt")
```

**Difference between `copy()` and `copy2()`:**

| `copy()` | `copy2()` |
|---|---|
| Copies file contents | Copies file contents |
| Preserves permission mode | Preserves permission mode |
| Does not attempt to preserve all metadata | Attempts to preserve additional metadata |

## C. `shutil.copyfile()`

Copies only the contents of a file.

```python
import shutil

shutil.copyfile("source.txt", "destination.txt")
```

Important:
- It copies file contents.
- It does not copy the permission mode or other metadata.
- The destination should not be the same file as the source.

---

# 3. Copying Complete Folders

## `shutil.copytree()`

Copies an entire directory, including its files and subdirectories.

```python
import shutil

shutil.copytree("data", "data_backup")
```

Example folder:

```text
data/
│
├── students.csv
├── marks.csv
└── reports/
    └── result.txt
```

After copying:

```text
data_backup/
│
├── students.csv
├── marks.csv
└── reports/
    └── result.txt
```

**Remember:** By default, the destination directory should not already exist.

---

# 4. Moving Files and Folders

## `shutil.move()`

Moves a file or directory to another location. It can also be used to rename a file or directory.

```python
import shutil

shutil.move("report.txt", "backup/report.txt")
```

Example of renaming:

```python
shutil.move("old_name.txt", "new_name.txt")
```

---

# 5. Deleting Folders

## `shutil.rmtree()`

Deletes a directory and everything inside it, including subdirectories.

```python
import shutil

shutil.rmtree("temporary_folder")
```

**Important Safety Warning:**

- This operation is destructive.
- Deleted files may not be recoverable.
- Never test it on important folders.
- Always create a temporary practice folder.
- Verify the exact folder path before deletion.
- Never use it on system folders, your home directory, or a project folder containing important work.

For safe practice, create a folder such as `test_delete_folder/` containing dummy files and delete only that folder.

---

# 6. Finding Executable Programs

## `shutil.which()`

Finds the location of an executable program using the system's executable search path.

```python
import shutil

location = shutil.which("python")

print(location)
```

If Python is available through the system's executable search path, its location is returned. Otherwise, the result is `None`.

---

# 7. Checking Disk Usage

## `shutil.disk_usage()`

Returns information about disk space.

```python
import shutil

usage = shutil.disk_usage("C:/")

print("Total:", usage.total)
print("Used:", usage.used)
print("Free:", usage.free)
```

It returns three values:

| Attribute | Meaning |
|---|---|
| `total` | Total disk space |
| `used` | Used disk space |
| `free` | Available disk space |

The values are in bytes.

---

# 8. Creating Archive Files

## A. `shutil.make_archive()`

Creates an archive from a directory.

```python
import shutil

shutil.make_archive(
    "backup",
    "zip",
    "data"
)
```

This creates a ZIP archive named `backup.zip` containing the contents of the `data` directory.

## B. `shutil.unpack_archive()`

Extracts an archive.

```python
import shutil

shutil.unpack_archive(
    "backup.zip",
    "extracted_data"
)
```

This extracts the archive into the `extracted_data` directory.

---

# 9. Important Concepts

| Concept | Description |
|---|---|
| `shutil` | Python module for high-level file operations |
| `copy()` | Copies a file and its permission mode |
| `copy2()` | Copies a file and attempts to preserve metadata |
| `copyfile()` | Copies file contents |
| `copytree()` | Copies a directory tree |
| `move()` | Moves or renames files and directories |
| `rmtree()` | Deletes a directory tree |
| `which()` | Finds an executable |
| `disk_usage()` | Checks disk usage |
| `make_archive()` | Creates an archive |
| `unpack_archive()` | Extracts an archive |

---

# 10. Practice Questions

Solve every question independently. Follow the requirements and steps instead of copying code.

## Level 1 — Basic Practice

### Q1. Copy a Text File

**Concept:** `shutil.copy()`

**Requirements:**
- Create a text file.
- Copy it to another location.
- Verify that the copied file exists.
- Display a success message.

**Steps to Solve:**
1. Import `shutil`.
2. Create a source text file with some content.
3. Select a destination path.
4. Use `shutil.copy()`.
5. Verify the destination file.
6. Display the result.

### Q2. Copy a File with Metadata

**Concept:** `shutil.copy2()`

**Requirements:**
- Create a sample file.
- Copy it using `copy2()`.
- Compare the source and destination modification times.
- Display both file paths.

**Steps to Solve:**
1. Import `shutil` and `os`.
2. Create a sample source file.
3. Copy it using `shutil.copy2()`.
4. Read the modification time of both files.
5. Compare the values.
6. Display the result.

### Q3. Copy Only File Contents

**Concept:** `shutil.copyfile()`

**Requirements:**
- Create a source file.
- Copy its contents into a new file.
- Read both files.
- Verify that their contents match.

**Steps to Solve:**
1. Create a source file.
2. Write some text into it.
3. Use `shutil.copyfile()`.
4. Open both files in read mode.
5. Compare their contents.
6. Display whether the copying was successful.

### Q4. Copy an Entire Folder

**Concept:** `shutil.copytree()`

**Requirements:**
- Create a folder.
- Add at least two files.
- Create a subfolder containing another file.
- Copy the complete folder.
- Verify the copied structure.

**Steps to Solve:**
1. Create a practice directory.
2. Add sample files and a subdirectory.
3. Select a new destination directory.
4. Use `shutil.copytree()`.
5. Check whether all files and subdirectories exist.
6. Display the result.

### Q5. Move a File

**Concept:** `shutil.move()`

**Requirements:**
- Create a source file.
- Create a destination folder.
- Move the source file into the destination folder.
- Verify the new location.

**Steps to Solve:**
1. Create a file.
2. Create a destination directory.
3. Use `shutil.move()`.
4. Check the original path.
5. Check the destination path.
6. Display the result.

---

## Level 2 — Logic Building

### Q6. Rename a File Using Shutil

**Concept:** `shutil.move()`

**Requirements:**
- Create a file with an old name.
- Rename it using `shutil.move()`.
- Check whether the old file exists.
- Check whether the renamed file exists.

**Steps to Solve:**
1. Create a sample file.
2. Decide its new name.
3. Use `shutil.move()` with the new path.
4. Verify the old path.
5. Verify the new path.
6. Display the renamed file information.

### Q7. Find Python Executable

**Concept:** `shutil.which()`

**Requirements:**
- Search for the Python executable.
- Display its location.
- Handle the case when it is not found.

**Steps to Solve:**
1. Import `shutil`.
2. Call `shutil.which()` with the executable name.
3. Store the returned value.
4. Check whether the value is `None`.
5. Display the location or a not-found message.

### Q8. Display Disk Information

**Concept:** `shutil.disk_usage()`

**Requirements:**
- Check disk usage for a drive.
- Display total space.
- Display used space.
- Display free space.
- Convert bytes into GB for easier reading.

**Steps to Solve:**
1. Import `shutil`.
2. Pass a valid drive path to `disk_usage()`.
3. Store the returned information.
4. Read total, used, and free values.
5. Convert bytes into GB.
6. Display all three values.

### Q9. Create a ZIP Backup

**Concept:** `shutil.make_archive()`

**Requirements:**
- Create a folder containing sample files.
- Create a ZIP archive from that folder.
- Verify that the ZIP file exists.
- Display a success message.

**Steps to Solve:**
1. Create a practice folder.
2. Add multiple sample files.
3. Select an archive name.
4. Use `shutil.make_archive()`.
5. Check whether the archive exists.
6. Display its path.

### Q10. Extract a ZIP File

**Concept:** `shutil.unpack_archive()`

**Requirements:**
- Use an existing ZIP archive.
- Extract it into a new folder.
- Verify the extracted files.
- Display the extraction result.

**Steps to Solve:**
1. Create or select a practice ZIP archive.
2. Choose a new extraction directory.
3. Use `shutil.unpack_archive()`.
4. Check the extracted directory.
5. Verify the expected files.
6. Display the result.

---

## Level 3 — Practical Problems

### Q11. Safe Temporary Folder Cleaner

**Concept:** `shutil.rmtree()`, `os.path`

**Requirements:**
- Create a dedicated temporary practice folder.
- Add dummy files and subfolders.
- Check whether the folder exists.
- Delete only that test folder.
- Verify that it has been deleted.

**Steps to Solve:**
1. Create a folder named `test_delete_folder`.
2. Add sample files and a subfolder.
3. Verify that the target path is exactly the test folder.
4. Check whether the folder exists.
5. Use `shutil.rmtree()` only on this test folder.
6. Verify that the folder no longer exists.
7. Never use this practice program on important directories.

### Q12. File Backup Manager

**Concept:** `shutil.copy2()`, `shutil.copytree()`

**Requirements:**
- Accept a source folder.
- Create a backup folder.
- Copy all files and subfolders.
- Preserve file metadata where supported.
- Display backup completion status.

**Steps to Solve:**
1. Accept or define a source directory.
2. Verify that the source directory exists.
3. Select a backup destination.
4. Use `shutil.copytree()` with an appropriate copy function.
5. Handle an existing destination directory.
6. Verify the copied files.
7. Display a backup summary.

---

# 11. Main Challenge — File Backup & Organizer Utility

**Project Name:** Smart File Backup Manager

Build a Python application that manages files and creates backups using the `shutil` module.

## Required Features

1. Copy a single file.
2. Copy a complete folder.
3. Move files into another folder.
4. Rename files.
5. Create ZIP backups.
6. Extract ZIP backups.
7. Display disk usage.
8. Find Python executable.
9. Display backup status.

## Requirements

- Use the `shutil` module.
- Use functions to separate each operation.
- Use `os` or `pathlib` to verify paths.
- Handle missing source files and folders.
- Handle existing destination paths.
- Display useful error messages.
- Use safe paths for all file operations.
- Do not delete important files.
- Keep the program modular and readable.

## Suggested Menu

```text
=====================================
       SMART FILE BACKUP MANAGER
=====================================

1. Copy File
2. Copy Folder
3. Move File
4. Rename File
5. Create ZIP Backup
6. Extract ZIP Backup
7. Check Disk Usage
8. Find Python Executable
9. Exit

Enter your choice:
```

## Suggested Project Structure

```text
Day30_Shutil_Module/
│
├── README.md
├── theory.py
├── practice.py
├── main.py
├── file_manager.py
├── backup_manager.py
└── test_files/
    ├── sample.txt
    └── documents/
        └── notes.txt
```

---

# 12. Debugging Practice

Find and fix the errors in these examples.

### Debugging Q1

```python
import shutil

shutil.copy("source.txt")
```

**Task:** Identify the missing argument and provide a valid destination path.

### Debugging Q2

```python
import shutil

shutil.copytree("source_folder", "source_folder")
```

**Task:** Identify why using the same source and destination is invalid. Choose a separate destination folder.

### Debugging Q3

```python
import shutil

shutil.move("missing.txt", "backup/missing.txt")
```

**Task:** Understand what happens when the source file does not exist. Add a check before moving it.

### Debugging Q4

```python
import shutil

shutil.rmtree("C:/")
```

**Task:** Explain why this is dangerous. Replace the target with a dedicated temporary practice folder and verify its path before deletion.

### Debugging Q5

```python
import shutil

usage = shutil.disk_usage("Z:/")

print(usage.total)
```

**Task:** Understand what happens if the drive does not exist. Add suitable path validation and error handling.

---

# 13. Interview Questions

1. What is the Python `shutil` module?
   **Answer:** It is a built-in module for high-level file and folder operations.
2. What does `shutil` stand for?
   **Answer:** It stands for **Shell Utilities**.
3. What is the purpose of `shutil.copy()`?
   **Answer:** It copies a file's contents and permission mode to a destination.
4. What is the difference between `copy()` and `copy2()`?
   **Answer:** `copy()` preserves permission mode; `copy2()` also tries to preserve extra metadata.
5. What does `copyfile()` copy?
   **Answer:** It copies only the contents of a file, not its metadata.
6. What is the purpose of `copytree()`?
   **Answer:** It copies a complete folder tree, including files and subfolders.
7. How is `move()` different from `copy()`?
   **Answer:** `copy()` leaves the original in place; `move()` transfers it to another location.
8. What does `rmtree()` do?
   **Answer:** It deletes a directory and everything inside it.
9. Why should `rmtree()` be used carefully?
   **Answer:** Because deletion is permanent/destructive and may remove important data.
10. What is the purpose of `shutil.which()`?
   **Answer:** It finds an executable's location using the system search path.
11. What information does `disk_usage()` return?
   **Answer:** It returns total, used, and free disk space in bytes.
12. What is the purpose of `make_archive()`?
   **Answer:** It creates an archive, such as a ZIP file, from files or a folder.
13. How do you extract an archive using Python?
   **Answer:** Use `shutil.unpack_archive(archive_path, destination_folder)`.
14. What happens if the destination folder already exists when using `copytree()`?
   **Answer:** By default, `copytree()` raises `FileExistsError` if the destination already exists.
15. How can you handle errors during file operations?
   **Answer:** Use checks and handle exceptions such as `FileNotFoundError`, `PermissionError`, and `OSError`.


---

# 14. Day 30 Completion Checklist

- [ ] Understand the `shutil` module.
- [ ] Practice `shutil.copy()`.
- [ ] Practice `shutil.copy2()`.
- [ ] Practice `shutil.copyfile()`.
- [ ] Practice `shutil.copytree()`.
- [ ] Practice `shutil.move()`.
- [ ] Understand safe use of `shutil.rmtree()`.
- [ ] Practice `shutil.which()`.
- [ ] Practice `shutil.disk_usage()`.
- [ ] Practice `shutil.make_archive()`.
- [ ] Practice `shutil.unpack_archive()`.
- [ ] Complete 12 practice questions.
- [ ] Solve 5 debugging questions.
- [ ] Complete Smart File Backup Manager.
- [ ] Answer interview questions.
- [ ] Push the work to GitHub.

---

# 15. GitHub Commit

```bash
git add .
git commit -m "Complete Day 30 Python Shutil Module Practice"
git push
```

---

# 🎯 Final Goal

After completing Day 30, I should be able to copy, move, organize, archive, extract, and back up files and folders using Python's `shutil` module.

> Always verify file paths before performing file operations.

> Practice destructive operations only inside temporary test folders.

> Understand the logic before writing the code.

**Day 30 Complete — Shutil Module in Python.**

---

<p align="center">
  <img src="https://img.shields.io/badge/Day%2030-Ready%20to%20Code%20%F0%9F%9A%80-22c55e?style=for-the-badge" alt="Day 28"/>
</p>

<h3 align="center"><b>Sudhanshu Dhande</b></h3>
<p align="center"><i>B.Tech (AI &amp; ML) · BATU, Lonere · Python OOP Journey</i></p>
