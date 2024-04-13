import re
from bs4 import BeautifulSoup


def clean_html_tags(raw_html):
    clean_text = BeautifulSoup(raw_html, "html.parser").text
    return clean_text


def remove_macros_and_headers(text):

    text = re.sub(r"^\s*\n", "", text, flags=re.MULTILINE)

    return text


def count_words(text):
    # Use regex to find words
    words = re.findall(r"\b\w+\b", text)
    return len(words)


def main():
    file_path = "src\\Base.tw"  # Replace with your actual file path
    cleaned_text = ""

    # Read the entire content of the Twee file
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if re.match(r"::\s*[^[\n]+", line):
            continue

        # Remove macros from the text
        cleaned_text += remove_macros_and_headers(line)

    # Count the words in the cleaned text
    print(cleaned_text)
    total_word_count = count_words(cleaned_text)

    # Output the total word count
    print(
        f"Total number of words in the file (excluding macros, HTML tags, and headers): {total_word_count}"
    )


if __name__ == "__main__":
    main()
