@echo off
SETLOCAL
IF "%PORT%"=="" SET PORT=5000
CALL venv\Scripts\activate
python -m waitress --host=0.0.0.0 --port=%PORT% wsgi:app
ENDLOCAL
