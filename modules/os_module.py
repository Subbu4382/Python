import os

#  Get the current working directory
print("Current Directory:", os.getcwd())

#  List files and folders in the current directory
print("Directory Contents:", os.listdir())

#  Create a new folder named 'my_folder'
os.mkdir("my_folder")

#  Remove a file named 'old_file.txt'
if os.path.exists("old_file.txt"):
    os.remove("old_file.txt")
    print("old_file.txt removed!")

#  Rename a file
if os.path.exists("old.txt"):
    os.rename("old.txt", "new.txt")
    print("File renamed to new.txt")

#  Change current working directory
os.chdir("my_folder")
print("Changed to:", os.getcwd())

#  Create folder if it doesn't exist
folder = "TestFolder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"{folder} created!")
else:
    print(f"{folder} already exists!")

#  Get file size (in bytes)
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"File size: {size} bytes")
else:
    print("data.txt not found.")
