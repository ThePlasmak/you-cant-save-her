import sys
import re

loading_background_color = "#030303"


def modify_html_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()

        # Replace the specified string
        file_contents = file_contents.replace(
            f"Helmet,Freesans,sans-serif;font-weight:700;color:#eee;background-color:#111;text-align:center",
            f"Helmet,Freesans,sans-serif;font-weight:700;color:{loading_background_color};background-color:{loading_background_color};text-align:center",
        )

        # Remove the specified string
        file_contents = re.sub(r"#init-loading\{[^\}]+\}", "", file_contents)

        # Write the modified contents back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_contents)

        print(f"{file_path} has been modified successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_html_file>")
    else:
        file_path = sys.argv[1]
        modify_html_file(file_path)
