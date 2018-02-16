## Sarabeth Jaffe

# Overview
This application is for the Udacity Full Stack Nanodegree project: Build an Item Catalog Application.

In this web app, the user is provided with a list of pre-populated categories and items as well as a user registration and authentication system (Google Accounts). Once logged in, the user will be able to post, edit, or delete their own items.

Bug: If Google Accounts authentication does not work in Google Chrome, try testing using Firefox.

# Resources/References:
1. Udacity
2. Github
3. [OAuth documentation](https://oauth.net/code/)
4. Stackoverflow
6. [SQL Alchemy](http://www.sqlalchemy.org/)

## Technologies Used
1. HTML
2. CSS
3. Python
4. OAuth
5. Python Flask Framework
6. SQLite / SQLAlchemy

## Dependencies
- Vagrant
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- VirtualBox
- Python 2.7+

## Setup
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal
6. If any packages need to be updated, run sudo pip install requests
7. Navigate to the `item-catalog-jaffe` folder, if not already in it.
8. Setup application database `python database_setup.py`
9. Insert fake data `python database_init.py`
10. Run application `python run_app.py`
11. Access the application locally by going to http://localhost:5000

## Using Google Login
To get the Google authentication to work:

1. Go to [Google Dev API](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials, then OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Inside the authorized JavaScript origins box input 'http://localhost:5000'
8. Inside the authorized redirect URIs boxes, input 
'http://localhost:5000/login' and 'http://localhost:5000/gconnect'
9. Click Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console click Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory 
14. Run application using `python run_app.py`

* If Google Account authentication does not work in Chrome, try Firefox.
