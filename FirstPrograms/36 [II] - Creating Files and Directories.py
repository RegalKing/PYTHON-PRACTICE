import os

# Method 1: Creating a File
def create_file_example():
    file_name = "new_file.txt"

    try:
        # Open the file in 'w' mode (write mode)
        # If the file doesn't exist, it will be created. If it exists, its existing content will be overwritten!
        with open(file_name, 'w') as file:
            file.write("This is a new file created using Python!\n")
            file.write("You can write data to this file.\n")
        print(f"File '{file_name}' created successfully.")
    except OSError:
        print("An error occurred while creating the file.")

# Method 2: Creating a Directory
def create_directory_example():
    directory_name = "new_directory"

    try:
        # Create a new directory
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

# Method 3: Creating Nested Directories
def create_nested_directory_example():
    nested_directory = "parent_dir/child_dir/grandchild_dir"

    try:
        # Create nested directories (multiple levels)
        os.makedirs(nested_directory)
        print(f"Nested directory '{nested_directory}' created successfully.")
    except FileExistsError:
        print(f"Nested directory '{nested_directory}' already exists.")

# Call each method to perform file and directory creation
create_file_example()
create_directory_example()
create_nested_directory_example()
