# Sarabeth Jaffe
# Linux Server Configuration project

# Required Information
## i. IP address and SSH port.
- Public IP address: 35.160.177.118
- SSH port: 2200

## ii. Complete URL to hosted web application.
URL to hosted webpage: http://ec2-35-160-177-118.us-west-2.compute.amazonaws.com/

## iii. Summary of software installed and configuration changes made.
Software installed:
- Apache2
- mod_wsgi
- PostgreSQL
- git
- pip
- virtualenv
- httplib2
- Python Requests
- oauth2client
- SQLAlchemy
- Flask
- libpq-dev
- Psycopg2

### Configuration steps:
1. Created + set up instance on Amazon Lightsail.
2. Connected to instance on local machine by saving private key.
3. Upgraded currently install packages.
4. Configured firewall.
- Changed SSH port from 22 to 2200
- Restricted firewall based on specifications in assignment: SSH (port 2200), HTTP (port 80), and NTP (port 123)
5. Created grader user account. Gave them admin permissions. Tested grader login using their key at port 2200.
6. Configured timezone to UTC.
7. Configured Apache2 server.
8. Installed & enabled mod_wsgi so that Flask application could be served up.
9. Installed psql & restricted remote connections.
10. Updated Python version.
11. Created psql user named catalog. Restricted their permissions to database only uses.
12. Created psql database.
13. Cloned item catalog project into /var/www folder. Modified file to work with psql instead of sqlite calls. Added absolute paths to database instead of relative.
14. Set up Google console Oauth permissions. Added client_secrets.json file to project directory. Added client-id to login.html file, and path to client_secrets.json file in __init__.
15. Installed pip. 
16. Created virtual environment. 
17. Activated environment and installed project dependencies (local to the venv).
18. Created + enabled virtual host / .conf file.
19. Created .wsgi file. 
20. Activated venv, ran database_setup.py, database_init.py. Deactivated the venv.
21. Restarted Apache2 server.
22. Navigated to application at Lightsail host.
23. Tested application functionality.

iv. A list of any third-party resources you made use of to complete this project.

- http://www.hcidata.info/host2ip.cgi
- http://flask.pocoo.org/docs/0.12/installation/
- https://www.tutorialspoint.com/postgresql/postgresql_create_database.htm
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
- http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#working-with-virtual-environments
- http://docs.sqlalchemy.org/en/latest/core/engines.html#configuring-logging
- A variety of posts on: https://discussions.udacity.com/c/nd004-p7-linux-based-server-configuration
- Udacity Linux Security Videos
- Udacity Web Application Server Videos
- https://stackoverflow.com/questions/40680109/sqlalchemy-import-issue-in-virtualenv

SSH key for grader in the "Notes to Reviewer" field.

Thanks!
