import sys
import re

loading_background_color = "#030303"


def modify_html_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()

        # Replace the loading background color
        file_contents = file_contents.replace(
            f"Helmet,Freesans,sans-serif;font-weight:700;color:#eee;background-color:#111;text-align:center",
            f"Helmet,Freesans,sans-serif;font-weight:700;color:{loading_background_color};background-color:{loading_background_color};text-align:center",
        )

        # Remove the init-loading part
        file_contents = re.sub(r"#init-loading\{[^\}]+\}", "", file_contents)

        # Prevent flash of unstyled content (edit: does not work)
        #         file_contents = file_contents.replace(
        #             f"""<meta charset="UTF-8" />""",
        #             f"""<meta charset="UTF-8" />
        # <style>html{{visibility: hidden;opacity:0;\}}</style>""",
        #         )

        # Add more meta tags
        file_contents = file_contents.replace(
            f"""<meta name="viewport" content="width=device-width,initial-scale=1" />""",
            f"""<meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="description" content="An interactive fiction game about fighting your former friend." />
<meta property="og:title" content="You Can&#39;t Save Her" />
<meta property="og:description" content="An interactive fiction game about fighting your former friend." />
<meta property="twitter:description" content="An interactive fiction game about fighting your former friend." />

<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="manifest" href="site.webmanifest">
<meta name="msapplication-TileColor" content="#2b5797">
<meta name="theme-color" content="#ffffff">""",
        )

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
