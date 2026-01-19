import os
import argparse
from PIL import Image
from pillow_heif import register_heif_opener
from tqdm.auto import tqdm

register_heif_opener()

def convert_to_jpg(input_path, remove_original=False):
    """Convert HEIC to JPG. Remove original file by option."""
    # Skip AppleDouble metadata files created by macOS
    if os.path.basename(input_path).startswith("._"):
        return

    try:
        output_path = os.path.splitext(input_path)[0] + ".jpg"
        img = Image.open(input_path)
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=95)
        
        if remove_original:
            os.remove(input_path)
    except Exception as e:
        print(f"\n[ERROR] Can't convert {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert HEICs in JPGs.")
    
    # Argument: path (file or folder accepted)
    parser.add_argument("path", help="path of file HEIC or folder containing HEIC files.")
    
    # Argument: flag -r to remove original file
    parser.add_argument("-r", "--remove", action="store_true", 
                        help="remove original HEIC file after successful operation.")

    args = parser.parse_args()
    target_path = args.path

    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' not exists.")
        return

    # Just a file
    if os.path.isfile(target_path):
        if target_path.lower().endswith(".heic"):
            convert_to_jpg(target_path, args.remove)
            print("Done.")
        else:
            print("File is not .heic")

    # a bunch of files (folder)
    elif os.path.isdir(target_path):
        all_files = []
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.lower().endswith(".heic") and not file.startswith("._"):
                    all_files.append(os.path.join(root, file))
        
        if not all_files:
            print("No HEIC found.")
            return

        for file_path in tqdm(all_files, desc="Working"):
            convert_to_jpg(file_path, args.remove)

if __name__ == "__main__":
    main()
