import os
from PIL import Image
import glob

def convert_to_webp(folder_path):
    print(f"Checking directory: {folder_path}")
    image_files = []
    image_files.extend(glob.glob(os.path.join(folder_path, '*.jpg')))
    image_files.extend(glob.glob(os.path.join(folder_path, '*.png')))
    image_files.extend(glob.glob(os.path.join(folder_path, '*.jpeg')))
    
    for filename in image_files:
        if filename.endswith('.webp'):
            continue
            
        print(f"Converting: {filename}")
        try:
            img = Image.open(filename)
            new_filename = os.path.splitext(filename)[0] + '.webp'
            img.save(new_filename, 'webp', quality=85)
            os.remove(filename)
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

def update_references(folder_path):
    # Find all HTML and CSS files
    files_to_check = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.endswith('.html') or f.endswith('.css'):
                files_to_check.append(os.path.join(root, f))
                
    for filepath in files_to_check:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('.jpg', '.webp').replace('.png', '.webp').replace('.jpeg', '.webp')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated references in {filepath}")

if __name__ == '__main__':
    base_dir = r'c:\Users\APEX\New folder\HAPPY-SALON-main'
    images_dir = os.path.join(base_dir, 'assets', 'images')
    
    convert_to_webp(base_dir)
    convert_to_webp(images_dir)
    
    update_references(base_dir)
    print("Done")
