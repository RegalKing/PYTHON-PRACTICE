import os
import shutil

# Method 1: Deleting a File using os.remove()
def delete_file_using_os_remove():
    file_to_delete = "deleteThisFile.txt"

    try:
        # Delete the file
        os.remove(file_to_delete)
        print(f"File '{file_to_delete}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_to_delete}' not found.")
    except PermissionError:
        print(f"Permission denied while trying to delete '{file_to_delete}'.")

# Method 2: Deleting a Directory using shutil.rmtree()
# THIS IS A VERY DANGEROUS FUNCTION USE IT WITH CAUTION - IT RECURSIVELY DELETES THE SPECIFIED DIRECTORY AND ALL ITS SUBDIRECTORIES AND FILES AND IS IRREVERSIBLE
def delete_directory_using_shutil_rmtree():
    directory_to_delete = "directory_to_delete"

    try:
        # Delete the directory and its contents
        shutil.rmtree(directory_to_delete)
        print(f"Directory '{directory_to_delete}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_to_delete}' not found.")
    except PermissionError:
        print(f"Permission denied while trying to delete '{directory_to_delete}'.")

# Call each method to perform the file and directory deletions
delete_file_using_os_remove()
delete_directory_using_shutil_rmtree()
