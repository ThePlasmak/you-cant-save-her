"""
Replaces the SugarCube format with your target format in a Twee file and exports it.
"""

import shutil
import os
import re

# Define the source and destination directories
source_dir = "src"
temp_dir = "enscree_temp"
export_name = "You_Can't_Save_Her_enscree"

# Ensure the destination directory exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Copy all files from src
for filename in os.listdir(source_dir):
    src_file = os.path.join(source_dir, filename)
    dest_file = os.path.join(temp_dir, filename)
    if os.path.isfile(src_file):
        shutil.copy(src_file, dest_file)

# Path to the Base.tw file in the destination directory
base_tw_path = os.path.join(temp_dir, "Base.tw")

# Read the content of Base.tw
with open(base_tw_path, "r", encoding="utf-8") as file:
    base_content = file.read()

# Replace the specific block of text in Base.tw
base_content = re.sub(
    r'"format":\s*"SugarCube",\s*"format-version":\s*"2.36.1",',
    r'"format": "Enscree",\n    "format-version": "1.1.1",',
    base_content,
    flags=re.DOTALL,
)

# Write the modified content back to Base.tw
with open(base_tw_path, "w", encoding="utf-8") as file:
    file.write(base_content)

# Export to Enscree format
os.system(f'call tweego -l -o "export/{export_name}.html" enscree_temp')
os.system(
    f'call tweego -l -o "C:/Users/Sarah/Documents/GitHub/theplasmak.github.io/private/{export_name}.html" enscree_temp'
)

# Check if the enscree_temp directory exists and delete it
if os.path.exists(temp_dir):
    try:
        shutil.rmtree(temp_dir)
        print(f"The directory {temp_dir} has been successfully deleted.")
    except Exception as e:
        print(f"Failed to delete {temp_dir}. Reason: {e}")

print("Enscree export attempt complete.")
