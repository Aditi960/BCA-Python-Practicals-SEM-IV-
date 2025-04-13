import os
import re

# Path to your target folder
folder_path = r"C:\Users\dell\OneDrive\Desktop\Adi's treasure\Python slips"

# Regex pattern for lines like: # Python code for Slip 19, Question 2
pattern = re.compile(r"# Python code for Slip \d{1,2}, Question [12]")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines()]

        # Delete if empty or contains only the Slip comment
        if not lines or (len(lines) == 1 and pattern.fullmatch(lines[0])):
            os.remove(file_path)
            print(f"Deleted: {filename}")