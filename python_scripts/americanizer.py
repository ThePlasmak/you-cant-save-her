import requests

def americanize(string):
    url = "https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/british_spellings.json"
    british_to_american = requests.get(url).json()    

    for british_spelling, american_spelling in british_to_american.items():
        string = string.replace(british_spelling, american_spelling)
  
    return string

def process_twine_file(input_file, output_file):
    # Read the content of the input Twine file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Americanize the content
    americanized_content = americanize(content)

    # Write the americanized content to the output Twine file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(americanized_content)

input_file = "C:\\Users\\Sarah\\Documents\\GitHub\\you-cant-save-her\\src\\Base.tw"
output_file = "C:\\Users\\Sarah\\Documents\\GitHub\\you-cant-save-her\\src\\Base.tw"

process_twine_file(input_file, output_file)
