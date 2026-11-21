# 13. Interview Questions

1. **What is the Python `shutil` module?**

    It is a built-in module for high-level file and folder operations.
2. **What does `shutil` stand for?**

    It stands for **Shell Utilities**.
3. **What is the purpose of `shutil.copy()`?**

    It copies a file's contents and permission mode to a destination.
4. **What is the difference between `copy()` and `copy2()`?**

   `copy()` preserves permission mode; `copy2()` also tries to preserve extra metadata.
5. **What does `copyfile()` copy?**

    It copies only the contents of a file, not its metadata.
6. **What is the purpose of `copytree()`?**

    It copies a complete folder tree, including files and subfolders.
7. **How is `move()` different from `copy()`?**

   `copy()` leaves the original in place; `move()` transfers it to another location.
8. **What does `rmtree()` do?**

   It deletes a directory and everything inside it.

9. **Why should `rmtree()` be used carefully?**

   Because deletion is permanent/destructive and may remove important data.

10. **What is the purpose of `shutil.which()`?**

    It finds an executable's location using the system search path.

11. **What information does `disk_usage()` return?**

    It returns total, used, and free disk space in bytes.

12. **What is the purpose of `make_archive()`?**

    It creates an archive, such as a ZIP file, from files or a folder.

13. **How do you extract an archive using Python?**

    Use `shutil.unpack_archive(archive_path, destination_folder)`.

14.**What happens if the destination folder already exists when using `copytree()`?**

    By default, `copytree()` raises `FileExistsError` if the destination already exists.

15. **How can you handle errors during file operations?**

    Use checks and handle exceptions such as `FileNotFoundError`, `PermissionError`, and `OSError`.
