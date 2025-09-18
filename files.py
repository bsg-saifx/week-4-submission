import csv
import json
import shutil
from pathlib import Path

def csv_to_json(csv_file,json_file):
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Converted {csv_file} to {json_file}")

def archieve_folder(folder,archieve):
    shutil.make_archive(archieve, 'zip', folder)
    print(f"Archived {folder} to {archieve}.zip")

def find_txt_file(directory):
    p = Path(directory)
    txt_files = list(p.rglob('*.txt'))
    return txt_files

if __name__ == "__main__":
    csv_to_json('data.csv', 'data.json')
    archieve_folder('my_directory', 'my_archive')
    txt_files = find_txt_file('.')
    print(f"Found {len(txt_files)} .txt files:")
    for file in txt_files:
        print(file)