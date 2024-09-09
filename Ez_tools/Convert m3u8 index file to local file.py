#Convert m3u8 index file to local file
import os

def replace_path_in_m3u8(file_path: str, old_path: str, new_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace(old_path, new_path)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Updated paths in {file_path}")

def traverse_and_replace(root_folder: str, old_path: str, new_path: str):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.m3u8'):
                file_path = os.path.join(dirpath, filename)
                replace_path_in_m3u8(file_path, old_path, new_path)

def main():
    root_folder = r'F:\Download'
    old_path = 'F:/Download'
    new_path = 'F:/Download/'
    
    traverse_and_replace(root_folder, old_path, new_path)

if __name__ == "__main__":
    main()