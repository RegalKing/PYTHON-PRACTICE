import shutil
import os

# Method 1: Using shutil.move()
# This method is a simple way to move a file from one location to another.
def move_using_shutil_move():
    source_file = "source.txt"
    destination_file = "destination_move1.txt"

    try:
        # Move the file from source to destination
        shutil.move(source_file, destination_file)
        print("File moved using shutil.move()")
    except FileNotFoundError:
        print("File not found while trying to move!")

# Method 2: Using os.rename()
# This method moves a file by renaming it to a new location. It can only move files within the same filesystem.
def move_using_os_rename():
    source_file = "source.txt"
    destination_file = "destination_move2.txt"

    try:
        # Rename (move) the file to the new destination
        os.rename(source_file, destination_file)
        print("File moved using os.rename()")
    except FileNotFoundError:
        print("File not found while trying to move!")

# Method 3: Using shutil.move() to move a directory
# This method can also move directories along with their contents.
def move_directory_using_shutil_move():
    source_directory = "source_dir"
    destination_directory = "destination_dir_move1"

    try:
        # Move the directory from source to destination
        shutil.move(source_directory, destination_directory)
        print("Directory moved using shutil.move()")
    except FileNotFoundError:
        print("Directory not found while trying to move!")

# Method 4: Using os.rename() to move a directory
# This method can move directories within the same filesystem.
def move_directory_using_os_rename():
    source_directory = "source_dir"
    destination_directory = "destination_dir_move2"

    try:
        # Rename (move) the directory to the new destination
        os.rename(source_directory, destination_directory)
        print("Directory moved using os.rename()")
    except FileNotFoundError:
        print("Directory not found while trying to move!")

# Call each method to perform the file moves
move_using_shutil_move()
move_using_os_rename()
move_directory_using_shutil_move()
move_directory_using_os_rename()
