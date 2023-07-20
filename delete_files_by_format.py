import os

def delete_files_by_format(file_paths, target_format):
    for file_path in file_paths:
        if os.path.splitext(file_path)[1].lower() == target_format:
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
