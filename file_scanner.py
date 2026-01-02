import os

def find_python_files(folder_path):
        python_files = []
    
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    python_files.append(full_path)
        
        return python_files