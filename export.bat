@REM call tweego -l -o "export\index.html" src
@REM python python_scripts/html_editor.py "export\index.html"

@REM call tweego -l -o "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html" src
@REM python python_scripts/html_editor.py "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html"

call tweego -l -o "testing\index.html" src
python python_scripts/html_editor.py "testing\index.html"

@REM Itch.io upload
@REM call butler push testing plasmak/you-cant-save-her:win-linux-mac-android

@REM ZIP for IFComp
@REM powershell -Command "New-Item -ItemType Directory -Force -Path 'temp_dir'; Copy-Item 'testing\*' 'temp_dir' -Recurse; Compress-Archive -Path 'temp_dir\*' -DestinationPath 'export/you-cant-save-her.zip' -Force; Remove-Item 'temp_dir' -Recurse"

@REM python python_scripts/twee_to_poof.py

@REM python python_scripts/twee_to_illume.py
@REM python python_scripts/twee_to_copypaste.py
@REM python python_scripts/twee_to_dotgraph.py
@REM python python_scripts/twee_to_dotscap.py
@REM python python_scripts/twee_to_enscree.py

@REM python python_scripts/twee_to_docx.py