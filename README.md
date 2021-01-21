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

Freeze the requirements file so that it is easy to port. 
```
pip freeze > requirements.txt 
# To reinstall on another machine 
pip install -r requirements.txt 
```

Make changes to settings.py file so that timezone is correctly set 
```
    TIME_ZONE = 'Asia/Kolkata'
```

Test on the local server 
```
# Make Migrations 
python manage.py makemigrations 
python manage.py migrate 

# Create a superuser 
python manage.py createsuperuser 

# Run a local server to test 
python manage.py 
```

You should have the django project up and running. Try loggin into the backend admin too. 

Notes and References
--------------------------------------------


