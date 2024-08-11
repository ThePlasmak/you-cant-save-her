@REM call tweego -l -o "export\index.html" src
@REM python python_scripts/html_editor.py "export\index.html"

@REM call tweego -l -o "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html" src
@REM python python_scripts/html_editor.py "C:\Users\Sarah\Documents\GitHub\theplasmak.github.io\private\You_Can't_Save_Her.html"

call tweego -l -o "testing\index.html" src
python python_scripts/html_editor.py "testing\index.html"
call butler push testing sarahmak/you-cant-save-her:win-linux-mac-android
powershell -Command "New-Item -ItemType Directory -Force -Path 'you-cant-save-her'; Copy-Item 'testing\*' 'you-cant-save-her' -Recurse; Compress-Archive -Path 'you-cant-save-her' -DestinationPath 'export/you-cant-save-her.zip' -Force; Remove-Item 'you-cant-save-her' -Recurse"

@REM python python_scripts/twee_to_poof.py

@REM python python_scripts/twee_to_docx.py