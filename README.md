# Sarabeth Jaffe
# Linux Server Configuration project

## i. The IP address and SSH port.

Public IP address: 35.160.177.118
SSH port: 2200

ii. The complete URL to your hosted web application.

URL to hosted webpage: http://ec2-35-160-177-118.us-west-2.compute.amazonaws.com/

iii. A summary of software you installed and configuration changes made.

Software installed:
Apache2
mod_wsgi
PostgreSQL
git
pip
virtualenv
httplib2
Python Requests
oauth2client
SQLAlchemy
Flask
libpq-dev
Psycopg2

Configuration steps:
1. Create + set up instance on Amazon Lightsail
2. Connected to instance on local machine by saving private key.
3. Upgraded currently install packages.
4. Configured firewall.
>>> Changes SSH port from 22 to 2200
>>> Restrict firewall based on specifications in assignment
5. Created grader account. Gave them admin permissions. Logged in as grader using their key at port 2200.
6. Configured timezone to UTC.
7. Configured Apache2 server.
8. Installed & enabled mod_wsgi so that Flask application could be served up.
9. Installed psql & restricted remote connections.
10. Updated Python version.
11. Created psql user named catalog. Restricted their permissions to database only uses.
12. Created psql database.
13. Cloned project into /var/www folder. Modified file to work with psql instead of sqllite calls. Added absolute paths instead of relative.
14. Set up Google console Oauth permissions. Added client_secrets.json file to project directory. Added client-id to login.html file, and path to client_secrets.json file in __init__.
15. Installed pip. 
16. Created virtual environment. 
17. Activated environment and installed project dependencies (local to the venv).
18. Create + enable virtual host/.conf file.
19. Create .wsgi file. 
20. Activate venv, run database_setup.py, database_init.py. Deactivate the venv.
21. Restart Apache2 server.
22. Navigate to application at Lightsail host.

iv. A list of any third-party resources you made use of to complete this project.

http://www.hcidata.info/host2ip.cgi
http://flask.pocoo.org/docs/0.12/installation/
https://www.tutorialspoint.com/postgresql/postgresql_create_database.htm
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#working-with-virtual-environments
http://docs.sqlalchemy.org/en/latest/core/engines.html#configuring-logging
A variety of posts on: https://discussions.udacity.com/c/nd004-p7-linux-based-server-configuration
Udacity Linux Security Videos
Udacity Web Application Server Videos
https://stackoverflow.com/questions/40680109/sqlalchemy-import-issue-in-virtualenv

SSH key for grader in the "Notes to Reviewer" field.

Thanks!
