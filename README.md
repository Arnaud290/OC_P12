+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

# PROJECT 12: Develop a secure back-end architecture using Django ORM

+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

## Context

Create a CRM (Customer Relationship Management) API with Django REST Framwork and PostgreSQL using an entity-relationship diagram. Access to the database must be secured. A Django administration interface must also be created.


## Installation

### 1 - Installation of PostgreSQL (on Linux UBUNTU with sudo)

    command : apt install postgresql postgresql-client

    command : systemctl enable --now postgresql

    at /etc/postgresql/{postgreSQL_version}/main/postgresql.conf
    delete # before " listen_addresses "
    update " listen_addresses = '*' " 

    at /etc/postgresql/{postgreSQL_version}/main/pg_hba.conf
    update " host    all             all             {ip_loop}/24            md5 " 
    
    command : systemctl restart postgresql

    update admin password :

        command : su - postgres

        command : psql -c "ALTER USER postgres WITH password 'newpassword'"

    create database user : 

        command : psql -c "CREATE USER userdb WITH password 'userdbpassword'"

    create new database :

        command : createdb epiceventsdb -O userdb    


#TO DO

### 1 - Installation of Python3, the virtual environment tool, the package manager (on Linux UBUNTU)

    $ sudo apt-get install python3 python3-venv python3-pip


### 2 - Setting up the virtual environment "env"

    1 - Access to the project directory:
            
            cd /softdesk example

    2 - Creation of the virtual environment:
            
            $ python3 -m venv env


### 3 - Opening the virtual environment and adding modules

            $ source env/bin/activate
            
            (env) $ pip install -r requirements.txt
            

### 4 - Modification of the file literview / literview / settings_example.py

    1 - Rename the settings_example.py file to settings.py

    2 - Modify the variable 'SECRET_KEY' in order to add a security key
        "django-insecure- (+ 50 random characters with uppercase,
        lowercase, numbers and special characters) "


## Using the program


### 1 - Launch

    1 - activation of the virtual environment in the home directory:

        source env/bin/activate

    2 - access to the softdesk directory:

        cd /softdesk

    3 - Launching the Django server

        ./manage.py runserver


### 2 - Using the API

    In order to test this API, 4 fictitious users are registered with some projects,
    problems and comments in the "db.sqlite3" database made available in the repository:

        - admin
        - arnaud
        - eric
        - claude

        the password for users: P@ssword1

    Access to the admin page is possible:

        Example on a local installation: http://127.0.0.1:8000/admin

        user: admin
        password: P@ssword1

    This allows full access (read and write) to the database tables.

    Command for creating an administrator:

        ./manage.py createsuperuser

    To have an initial database:

        1 - Stop the Django server by performing the combination:
                
                 control + c

        2 - Delete the "db.sqlite3" file

        3 - migrate to the new base

                ./manage.py makemigrations => This creates a file in softdesk/projects/migrations

                ./manage.py migrate => Creation of tables in the "db.sqlite" file (created directly)
              
### 3 - Using queries

    Several methods exist to perform queries, example:

        - With POSTMAN software (Used for the documentation of this API)

                Installation on Linux UBUNTU:

                sudo snap install postman

        - With the command line software cURL:

            Installation on Linux UBUNTU:

                sudo snap install curl

            Example of the 'GET projects' request

                curl --location --request GET 'http://127.0.0.1:8000/projects' \
                --header 'Authorization: Bearer "TOKEN 'access' "'

### 4 - List of requests

    Detailed documentation is available at: https://documenter.getpostman.com/view/15579831/TzRVg6iY

    - POST signup: http://127.0.0.1:8000/signup/

        Registration of a user to the API.
        Fields to use: username, password, password2, first_name, last_name, email

    - POST: http://127.0.0.1:8000/login/

        Connection of a user to the API.
        Fields to use: username, password
        Return: TOKEN 'access' key (To be used for requests with authentication, valid for 1 hour)
                 TOKEN 'refresh' key (To be used for refresh and logout requests)
                 
    - POST: http://127.0.0.1:8000/login/refresh/

        Retrieving another pair of TOKEN keys without reconnecting
        Fields to use: refresh
        Return: TOKEN 'access' key (To be used for requests with authentication, valid for 1 hour)
                 TOKEN 'refresh' key (To be used for refresh and logout requests)

    - PUT: http://127.0.0.1:8000/change_password/

        Authentication required
        Allows the password to be changed
        Fields to use: old_password, password, password2

    - GET: http://127.0.0.1:8000/users/

        Authentication required
        Provides access to the list of API users

    - POST: http://127.0.0.1:8000/logout/
        Authentication required
        Allows you to blacklist the TOKEN refresh key to prohibit its use
        Fields to use: refresh

    - GET: http://127.0.0.1:8000/projects/

        Authentication required
        Access to the list of projects to which the user is linked.

    - POST: http://127.0.0.1:8000/projects/

        Authentication required
        Creation of a project
        Fields to use: title, description, project_type

    - GET: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user contributing to the project
        Access to project details
    
    - PUT: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user author of the project
        Modification of the project
        Fields to use: title, description, project_type

    - DELETE: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user author of the project
        Deleting the project

    - GET: http://127.0.0.1:8000/projects/{project_id}/users/
        
        Authentication required, user contributing to the project
        Access to the list of project contributors

    - POST: http://127.0.0.1:8000/projects/{project_id}/users/

        Authentication required, user author of the project
        Adding a contributor to the project
        Fields to use: user_id, role

    - DELETE: http://127.0.0.1:8000/projects/{project_id}/users/{user_id}

        Authentication required, user author of the project
        Removing a contributor from the project
     
    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/

        Authentication required, user contributing to the project
        Access to the list of project problems

    - POST: http://127.0.0.1:8000/projects/{project_id}/issues/

        Authentication required, user contributing to the project
        Adding a problem to the project
        Fields to use: title, description, tag, priority, status, assignee_user_id

    - PUT: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}

        Authentication required, user responsible for posted problem
        Adding a problem to the project
        Fields to use: title, description, tag, priority, status, assignee_user_id
    
    - DELETE: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}

        Authentication required, user responsible for posted problem
        Removing a problem from the project

    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/{{issue_id}/comments

        Authentication required, user contributing to the project
        Access to the list of comments on the problem

    - POST: http://127.0.0.1:8000/projects/{project_id}/issues/{{issue_id}/comments

        Authentication required, user contributing to the project
        Adding a comment to the problem
        Fields to use: description

    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user contributing to the project
        Access to the details of the comment to the problem

    - PUT: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user commenting
        Editing a comment to the problem
        Fields to use: description

    - DELETE: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user commenting
        Deleting a comment to the problem


