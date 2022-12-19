

### How to run pure python project:

1. Download the zip file of the project via github
   1. Click the green '<> Code' dropdown button
   2. Click "Download Zip"
2. Open a terminal window and navigate to the project using the `cd` command.
3. Run the code using this command `python3 BlackJack.py`

It's as simple as that!

### How to run django application:

Make sure you have python3 installed. To do this, run the following command: 
`python3 --version`
After opening your chosen IDE (I used PyCharm), follow these instructions: 

1. Using the terminal, clone the repository using these commands in the terminal (if you've already done this step, feel free to skip this!):
`git clone https://github.com/oliweisy99/BBCBlackJack.git` 
2. Create your own virtual environment using these commands: 
`python3 -m venv venv`
and then:\
`source venv/bin/activate`
   1. If you had trouble using venv, it is likely you'll need to run `pip install venv` first!
5. Run this command in the terminal to download all requirements:
`pip install -r requirements.txt`
6. Run these two commands in the terminal to setup the database:
`python manage.py makemigrations`
and then:
`python manage.py migrate`
7. Now you're ready to run the program. Run this command in the terminal:
`python manage.py runserver`

If further errors are encountered, make sure you follow the installation guidance here: https://docs.djangoproject.com/en/4.1/intro/install/


#### Versions:

Django: 4.1.4 \
Python: 3.8.5