import os

# Function to delete temporary files
def delete_temp_files(file_paths):
    for file_path in file_paths:
        try:
            # Delete the file
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")