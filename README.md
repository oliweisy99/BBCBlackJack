

## How To Run (Pure) Python Project:

1. Download the zip file of the project via github
   1. Click the green '<> Code' dropdown button
   2. Click "Download Zip"
2. Open a terminal window and navigate to the PurePythonProject directory using the `cd` command.
3. Run the code using this command in the terminal: `python3 BlackJack.py`

It's as simple as that!

## How To Run Django Application:

Make sure you have python3 installed. To do this, run the following command: 
`python3 --version`
After opening your chosen IDE (I used PyCharm), follow these instructions: 

1. Using the terminal, clone the repository using these commands (if you've already done this step, feel free to skip this!):
`git clone https://github.com/oliweisy99/BBCBlackJack.git`
2. Once you've cloned the project, direct yourself to the "DjangoProject" directory in the terminal, using the `cd` command
3. Create your own virtual environment by typing these commands into the terminal: 
`python3 -m venv venv`
and then:\
`source venv/bin/activate`
   1. If you had trouble using venv, it is likely you'll need to run `pip install venv` first!
4. Run this command in the terminal to download all requirements (this make take some time):
`pip install -r requirements.txt`
5. Run these two commands in the terminal to set up the database:
`python manage.py makemigrations`
and then:
`python manage.py migrate`
6. Now you're ready to run the program. Run this command in the terminal:
`python manage.py runserver`
7. The final step is to open a browser and type in `http://127.0.0.1:8000/` as the url.


If further errors are encountered, make sure you follow the installation guidance here: https://docs.djangoproject.com/en/4.1/intro/install/


![BlackJackGamePlay](https://github.com/oliweisy99/BBCBlackJack/blob/main/gameplayPhotos/img_1.png?raw=true)

#### Versions:

Django: 3.1.1 \
Python: 3.8.5