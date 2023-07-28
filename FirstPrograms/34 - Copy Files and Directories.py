
import shutil

# Method 1: Using shutil.copy()
# This method is a straightforward way to copy a file. THIS FUNCTION CAN ALSO COPY DIRECTORIES
def copy_using_shutil_copy():
    source_file = "copyfrom.txt"
    destination_file = "copyto.txt"

    # Copy the file from source to destination
    shutil.copy(source_file, destination_file)

# Method 2: Using shutil.copy2()
# This method is similar to shutil.copy(), but it preserves the original file's metadata. HIS FUNCTION CAN ALSO COPY DIRECTORIES
def copy_using_shutil_copy2():
    source_file = "copyfrom.txt"
    destination_file = "copyto.txt"

    # Copy the file from source to destination, preserving metadata
    shutil.copy2(source_file, destination_file)

# Method 3: Using shutil.copyfile()
# This method copies the contents of the source file to the destination file.
# It doesn't preserve metadata.
def copy_using_shutil_copyfile():
    source_file = "copyfrom.txt"
    destination_file = "copyto.txt"

    # Copy the contents of the source file to the destination file
    shutil.copyfile(source_file, destination_file)

# Method 4: Using File Handling (Manual Approach)
# You can manually read the contents of the source file and write them to the destination file.
def copy_using_file_handling():
    source_file = "copyfrom.txt"
    destination_file = "copyto.txt"

    # Open the source file in read mode
    with open(source_file, "r") as source:
        # Open the destination file in write mode
        with open(destination_file, "w") as destination:
            # Read the source file line by line and write it to the destination file
            for line in source:
                destination.write(line)

# Call each method to perform the file copies
copy_using_shutil_copy()
copy_using_shutil_copy2()
copy_using_shutil_copyfile()
copy_using_file_handling()

print("Files copied successfully!")
