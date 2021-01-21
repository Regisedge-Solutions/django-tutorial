Django - Tutorial
==================

This is a step-by-step quick tutorial to help new developers quickly onboard Django. 

Step 1 : Initial setup
--------------------------------------------

Create a virtual environment 

```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install django
```

Check the django-admin version and start the project 

```
django-admin --version
django-admin startproject myproject
```

Make changes to settings.py file so that timezone is correctly set 
```
    TIME_ZONE = 'Asia/Kolkata'
```


Notes and References
--------------------------------------------


