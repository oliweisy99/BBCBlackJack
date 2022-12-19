

### How to run pure python project:



### How to run django application:

1. Open application code in your IDE
   1. Using `cd yourDirectoryOrFile/` in the terminal to traverse into the "DjangoProject" directory 
2. Run this command in the terminal to download all requirements:
`pip install -r requirements.txt`
   1. If errors are encountered, make sure you follow the installation guidance here: https://docs.djangoproject.com/en/4.1/intro/install/

3. Run these two commands in the terminal to setup the database:
`python manage.py makemigrations`
and then:
`python manage.py migrate`

4. Now you're ready to run the program. Run this command in the terminal:
`python manage.py runserver`

#### Versions:

Django: 4.1.4 \
Python: 3.8.5