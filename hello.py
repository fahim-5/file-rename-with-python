import os

def rename_pictures(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only files with .png extension
    png_files = [file for file in files if file.endswith('.png')]
    
    # Sort the files to maintain a consistent order
    png_files.sort()

    # Rename each file
    for index, filename in enumerate(png_files):
        new_name = f"Picture_{index + 1}.png"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Specify the folder containing the pictures
folder_path = r"C:\Users\Asus\Desktop\Versa Stack Engineering\Back-End Tools\07__DataBase\Notes"

# Run the rename function
rename_pictures(folder_path)
