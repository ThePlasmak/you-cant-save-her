import shutil
import os
import re

# Define the source and destination directories
source_dir = "src"
temp_dir = "poof_temp"
export_name = "You_Can't_Save_Her_poof"

# Ensure the destination directory exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Copy all files from src to poof
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
    r'"format": "SugarCube",\s+"format-version": "2.36.1",',
    r'"format": "poof",\n    "format-version": "1.9.0",',
    base_content,
)

# Add additional text below the specified point
base_content = re.sub(
    r'("zoom": 1\n})',
    r"""\1

:: poof.config
{
    "nightMode": true,
    "codeHeightLimit": false,
    "ignoreTag": "widget",
    "format": {
        "name": "SugarCube",
        "version": "2.36.1"
    },
    "pdf" : {
        "lineHeight": 1.2,
        "font": "serif"
    },
    "parse": true
}
""",
    base_content,
)

# Write the modified content back to Base.tw
with open(base_tw_path, "w", encoding="utf-8") as file:
    file.write(base_content)

# Export to Poof format
os.system(f'call tweego -l -o "export/{export_name}.html" poof_temp')
os.system(
    f'call tweego -l -o "C:/Users/Sarah/Documents/GitHub/theplasmak.github.io/private/{export_name}.html" poof_temp'
)

# Check if the poof_temp directory exists and delete it
if os.path.exists(temp_dir):
    try:
        shutil.rmtree(temp_dir)
        print(f"The directory {temp_dir} has been successfully deleted.")
    except Exception as e:
        print(f"Failed to delete {temp_dir}. Reason: {e}")

print("Poof export attempt complete.")
