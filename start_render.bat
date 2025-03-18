@echo off
SETLOCAL
IF "%PORT%"=="" SET PORT=5000
CALL venv\Scripts\activate
gunicorn wsgi:app
ENDLOCAL
