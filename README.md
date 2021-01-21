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
    python manage.py  
   ```    

You should have the django project up and running. Try loggind into the backend admin too. 

Homework: Change the settings file to use postgres instead of sqlite.




<!-- REFERENCES -->
## Acknowledgements and References

* [README template](https://github.com/othneildrew/Best-README-Template)

<!-- CONTACT -->
## Contact

Abhinav Jain - abhinav@regisedge.com
Project Link: [https://github.com/Regisedge-Solutions/django-tutorial](https://github.com/Regisedge-Solutions/django-tutorial)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jabhinav/
