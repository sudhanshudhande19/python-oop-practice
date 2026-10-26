# Write a program that counts the files in a directory.

# Requirements:

    # Count files only, not subdirectories.
    # Display the total count.
    # Test an empty directory.

#------------------------------------------------------------------------------------------------

import os 

user = input('Enter The directory =')
count = 0
if os.path.exists(user) and os.path.isdir(user):

    contents = os.listdir(user)

    print('contents of directory :')

    for item in contents:
        count += 1
    print('file =',count)
else:
    print('directory does not exist or the path is invalid')
    