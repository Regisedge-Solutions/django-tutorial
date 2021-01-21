<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Regisedge-Solutions/django-tutorial">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django Tutorial</h3>

  <p align="center">
    This is a step-by-step quick tutorial to help new developers quickly familiarize with basic Django building blocks.  
    <br />
    <a href="https://github.com/Regisedge-Solutions/django-tutorial"><strong>Explore the Tutorial »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#tutorial-steps">Tutorial Steps</a>
      <ul>
        <li><a href="#step-1-initial-setup">Step 1 : Initial Setup</a></li>
        <li><a href="#step-2-adding-apps-and-defining-models">Step 2 : Adding apps and defining models</a></li>
        <li><a href="#step-3-managing-django-admin">Step 3 : Managing Django Admin</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgements-and-references">Acknowledgements and References</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- Tutorial Steps -->
## Tutorial steps 

<!-- STEP 1 -->
### Step 1 Initial Setup

1. Create a virtual environment 
   ```sh
    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install django
   ```
2. Check the `django-admin` version and start the project 
   ```sh
    django-admin --version
    django-admin startproject myproject
   ```
3. Freeze the requirements file so that it is easy to port. 
   ```sh
    pip freeze > requirements.txt 
    # To reinstall on another machine 
    pip install -r requirements.txt 
   ```    
4. Make changes to `settings.py` file so that timezone is correctly set 
    `TIME_ZONE = 'Asia/Kolkata'`
5. Test on local server
   ```sh
    # Make Migrations 
    python manage.py makemigrations 
    python manage.py migrate 

    # Create a superuser 
    python manage.py createsuperuser 

    # Run a local server to test 
    python manage.py runserver
   ```    

You should have the django project up and running. Try loggind into the backend admin too. 

Homework: Change the settings file to use postgres instead of sqlite.

<!-- STEP 2 -->
### Step 2 Adding apps and defining models

1. Create the customer and interaction models 
   ```sh
    python manage.py startapp customers
    python manage.py startapp interactions 
   ```
2. Create `urls.py` in customer and interactions apps 
3. Add the `urls.py` in the website's `url.py` routing files
4. Register the apps in the website's `setttings.py` file 
5. Define the models in the respective `models.py` files of the apps 
6. Make migrations and migrate the models
7. Notes 
    * Always use singular while creating models
    * While creating relationships, only add to one of the models - ManytoMany (any of the two) or ForeignKey (the one which contains)
    * Generally a good practice to extend the user model [Extending Link](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
    * Reference for different fields types [Official Model Documentation](https://docs.djangoproject.com/en/3.0/topics/db/models/)


<!-- STEP 3 -->
### Step 3 Managing Django Admin

1. Django bulk import-export functionality 
    ```sh
    pip install django-import-export
    # In settings.py
    #   Add import_export in installed apps in settings.py
    #   STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
    #   IMPORT_EXPORT_USE_TRANSACTIONS = True
    python manage.py collectstatic
   ```
2. Register the models to be used in `admin.py` files in the respective apps 
    * Look at the sample files to see how to customize list and detail view for various models
3. Basic admin configurations 
    * Change header using `admin.site.site_header` in any of the admin file
4. Notes 
    * [Reference for Import-Export](https://django-import-export.readthedocs.io/en/latest/installation.html)
    * Extend ModelAdmin in admin.py [Link](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-options)
    * DjangoAdmin Cookbook [Link](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)
    * Sometimes you might want to register a model to multiple ModelAdmin (e.g. Leaflet and ImportExportModelAdmin), in this case use proxy models 
    * Technically you can have multiple ModelAdmin for the same model
    * Ability to create inline forms in admin
    * Filters 
        * Django advanced filters for admin 
        * You can add multiple search fields in listview. Also you can add Foreign Key as __ to search
        * Ading autocomplete in django admin filters : https://medium.com/cashify-engineering/autocomplete-list-filter-in-django-admin-2a88ead52246 
    * You can create multiple admins for the same website :- e.g. basic-admin and advanced-admin
    * Have more hyperlinks to ForeignKey fields from the listView [Link](https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html)



<!-- REFERENCES -->
## Acknowledgements and References

* [README template](https://github.com/othneildrew/Best-README-Template)
* [Official Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

<!-- CONTACT -->
## Contact

Abhinav Jain - abhinav@regisedge.com

Project Link: [https://github.com/Regisedge-Solutions/django-tutorial](https://github.com/Regisedge-Solutions/django-tutorial)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jabhinav/
