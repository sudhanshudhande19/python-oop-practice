# Write a program that displays all files and folders inside a specified directory.

# Requirements:

    # Accept a directory path.
    # Display the names of its contents.
    # Handle a directory that does not exist.

#-----------------------------------------------------------------------------------------------------------



import os 

user = input('Enter The directory =')

if os.path.exists(user) and os.path.isdir(user):

    contents = os.listdir(user)

    print('contents of directory :')

    for item in contents:
        print(item)

else:
    print('directory does not exist or the path is invalid')
    