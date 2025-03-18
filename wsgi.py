echo from app import create_app > wsgi.py
echo. >> wsgi.py
echo app = create_app() >> wsgi.py
echo. >> wsgi.py
echo if __name__ == "__main__": >> wsgi.py
echo     app.run(debug=True) >> wsgi.py
