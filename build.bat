call tweego -l -o "testing\Advanced_Creative_Writing.html" src
python python_scripts/loading_screen_remover.py "testing\Advanced_Creative_Writing.html"

call tweego -l -o "export\Advanced_Creative_Writing.html" src
python python_scripts/loading_screen_remover.py "export\Advanced_Creative_Writing.html"

call tweego -l -o "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\Advanced_Creative_Writing.html" src
python python_scripts/loading_screen_remover.py "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\Advanced_Creative_Writing.html"

python python_scripts/twee_to_poof.py

python python_scripts/twee_to_docx.py