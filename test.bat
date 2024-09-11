@REM Create the "testing" folder if it doesn't exist
if not exist "testing" mkdir testing

@REM Constantly recompiles when it detects changes in src
call tweego -l -o "testing\index.html" src --watch