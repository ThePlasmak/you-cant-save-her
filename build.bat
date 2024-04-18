call tweego -l -o "testing\You_Can't_Save_Her.html" src
python python_scripts/loading_screen_remover.py "testing\You_Can't_Save_Her.html"

call tweego -l -o "export\You_Can't_Save_Her.html" src
python python_scripts/loading_screen_remover.py "export\You_Can't_Save_Her.html"

call tweego -l -o "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html" src
python python_scripts/loading_screen_remover.py "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html"

python python_scripts/twee_to_poof.py

python python_scripts/twee_to_docx.py