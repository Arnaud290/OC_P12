+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

# PROJECT 12: Develop a secure back-end architecture using Django ORM

+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

## Context

Create a CRM (Customer Relationship Management) API with Django REST Framwork and PostgreSQL using an entity-relationship diagram. Access to the database must be secured. A Django administration interface must also be created.


## Installation

### 1 - Installation of PostgreSQL and packages for psycopg2 driver (on Linux UBUNTU)

    sudo apt install postgresql postgresql-client libpq-dev python3-dev build-essential python3-psycopg2

    sudo systemctl enable --now postgresql

    at /etc/postgresql/{postgreSQL_version}/main/postgresql.conf
    delete # before " listen_addresses "
    update " listen_addresses = '127.0.0.1' " (for localhost or another client address)

    
    sudo systemctl restart postgresql

    update admin password :

        sudo su - postgres

        $ psql -c "ALTER USER postgres WITH password 'newpassword'"

    create database user : 

        $ psql -c "CREATE USER adminbdd WITH password 'userdbpassword'"

    create new database :

        $ createdb epiceventsdb -O adminbdd    


### 2 - Installation of Python3, the virtual environment tool, the package manager and git (on Linux UBUNTU)

    $ sudo apt-get install python3 python3-venv python3-pip git


### 3 - Clone project

    git clone https://github.com/Arnaud290/OC_P12.git

### 4 - Setting up the virtual environment "env"

    1 - Access to the project directory:
            
            $ cd OC_P12/

    2 - Creation of the virtual environment:
            
            $ python3 -m venv env


### 5 - Opening the virtual environment and adding modules

            $ source env/bin/activate
            
            (env) $ pip install -r requirements.txt


### 6 - Modification of the file settings_example.py

    (env) $ cd OC_P12/epiceventscrm/epiceventscrm/

    1 - Rename the settings_example.py file to settings.py

        (env) $ mv settings_exemple.py settings.py

    2 - In the settings.py file:

            modify the variable 'SECRET_KEY' in order to add a security key
            "django-insecure- (+ 50 random characters with uppercase,
            lowercase, numbers and special characters)

            in DATABASES :
            update password
            'PASSWORD': 'password_adminbdd',
        

### 7 - Migrate database and restaure dump db
            
            (env) $ cd OC_P12/epiceventscrm/
            (env) $ ./manage.py migrate
            sudo su
            su postgres 
            # cd OC_P12/epiceventscrm/db_file/
            # pg_restore --clean --dbname epiceventsdb epiceventsdb.dump

            if you want dump database: 

                # pg_dump --format=custom --file epiceventsdb.dump epiceventsdb


## Using the program


### 1 - Launch

    Launching the Django server

    (env) $ cd OC_P12/epiceventscrm/
    (env) $ ./manage.py runserver


### 2 - Using the CRM

    In order to test this CRM, 5 fictitious users are registered with some projects,
    problems and comments in the "db.sqlite3" database made available in the repository:

        - admin     > Manager user

        - françois  > Commmercial user
        - marc      > Commercial user

        - sylvain   > Support user
        - sophie    > Support user 

        the password for users: P@ssword1

    Access to the admin page :

        Example on a local installation:    http://127.0.0.1:8000/admin                 > Admin page
                                            http://127.0.0.1:8000/admin/log_viewer/     > Console log page

        user: admin
        password: P@ssword1

        Command for creating an administrator:

            (env) $ cd OC_P12/epiceventscrm/
            (env) $ ./manage.py createsuperuser

    Section of the admin page :

        CLIENT
            clients
                > view list
                > view object
                > create object
                > modify object
                > delete object

        CONTACT
            Contacts
                > view list
                > view object
                > create object
                > modify object
                > delete object

        CONTRACT
            Contracts
                > view list
                > view object
                > create object
                > modify object
                > delete object (if no event is associated)

            Status        
                > view list
                > view object
                > create object
                > modify object
                > delete object (if no contract is associated)

        EVENT
            Events
                > view list
                > view object
                > create object
                > modify object
                > delete object 

            Status        
                > view list
                > view object
                > create object
                > modify object
                > delete object (if no event is associated)

        MIDDLEWARE
            contact logs
                > view list
              
### 3 - Using queries

    Several methods exist to perform queries, example:

        - With POSTMAN software (Used for the documentation of this CRM)

                Installation on Linux UBUNTU:

                sudo snap install postman

        - With the command line software cURL:

            Installation on Linux UBUNTU:

                sudo snap install curl

            Example of the 'GET contract' request

                curl --location --request GET 'http://127.0.0.1:8000/contract' \
                --header 'Authorization: Bearer TOKEN_ACCESS'

### 4 - List of requests

    List of requests is available at: https://documenter.getpostman.com/view/15579831/TzeZDRMD

    LOGIN

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

        - POST: http://127.0.0.1:8000/logout/

            Authentication required
            Allows you to blacklist the TOKEN refresh key to prohibit its use
            Fields to use: refresh
            
    CONTACT

        - GET: http://127.0.0.1:8000/contact/

            Authentication required
            Commercial access:  Provides access to the list of support contacts
            Support Access:     Not allowed
            Admin access:       Provides access to the list of contacts

        - GET: http://127.0.0.1:8000/contact/{contact_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Returns the contact informations

        - POST http://127.0.0.1:8000/client/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Create a contact with first name, last name, email, mobile, password, password2, is_superuser, is_staff, is_active, post

        - PUT http://127.0.0.1:8000/contact/{contact_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Modify a contact informations, the user must enter all fields. For a partial modification, the PATCH action is available

        - DELETE http://127.0.0.1:8000/client/{client_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Delete the contact object

    CLIENT 

        - GET: http://127.0.0.1:8000/client/

            Authentication required
            Commercial access:  Returns the list of clients to which the commercial is linked
            Support Access:     Returns the list of clients to which support has a related event
            Admin access :      Returns the list of clients

        - GET: http://127.0.0.1:8000/client/{client_id}/

            Authentication required
            Commercial access:  Returns the client informations if the commercial user is linked
            Support Access:     Returns the client informations if the support user is linked by an event
            Admin access :      Returns the client informations

        - POST http://127.0.0.1:8000/client/

            Authentication required
            Commercial access:  Create a client with first name, last name, email, mobile, phone (optional), company name
            Support Access:     Not allowed
            Admin access :      Create a client with first name, last name, email, mobile, phone (optional), company name

        - PUT http://127.0.0.1:8000/client/{client_id}/

            Authentication required
            Commercial access:  Modify a client informations only if the commercial user is linked, the user must enter all fields
                                For a partial modification, the PATCH action is available
            Support Access:     Not allowed
            Admin access :      Modify a client informations, the user must enter all fields. For a partial modification, the PATCH action is available

        - DELETE http://127.0.0.1:8000/client/{client_id}/

            Authentication required
            Commercial access:  Deletes the client object only if the commercial user is linked and no contracts and events are linked
            Support Access:     Not allowed
            Admin access :      Delete the client object only if no contracts and events are linked

    CONTRACT

        - GET: http://127.0.0.1:8000/contract/

            Authentication required
            Commercial access:  Returns the list of contracts to which the commercial user is linked
            Support Access:     Not allowed
            Admin access :      Returns the list of contracts

        - GET: http://127.0.0.1:8000/contract/{contract_id}/

            Authentication required
            Commercial access:  Returns the contract informations if the commercial user is linked
            Support Access:     Not allowed
            Admin access :      Returns the contract informations

        - POST http://127.0.0.1:8000/contract/

            Authentication required
            Commercial access:  Create a contract with text, amount, status id, client id
            Support Access:     Not allowed
            Admin access :      Create a contract with text, amount, status id, client id
        
        - PUT http://127.0.0.1:8000/contract/{contract_id}/

            Authentication required
            Commercial access:  Modify a contract informations only if the commercial user is linked, the user must enter all fields
                                For a partial modification, the PATCH action is available
            Support Access:     Not allowed
            Admin access :      Modify a contract informations, the user must enter all fields
                                For a partial modification, the PATCH action is available
        
        - DELETE http://127.0.0.1:8000/contract/{contract_id}/

            Authentication required
            Commercial access:  Deletes the contract object only if the commercial user is linked and no events are linked
            Support Access:     Not allowed
            Admin access :      Delete the contract object only if no events are linked and no events are linked

    CONTRACT STATUS

        - GET: http://127.0.0.1:8000/status_contract/

            Authentication required
            Commercial access:  Returns the list of status contracts
            Support Access:     Not allowed
            Admin access :      Returns the list of status contracts

        - GET: http://127.0.0.1:8000/status_contract/{status_contract_id}

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Returns the status contract informations

        - POST http://127.0.0.1:8000/status_contract/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Create a status contract with status name

        - PUT http://127.0.0.1:8000/status_contract/{status_contract_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Modify a status contract informations, the user must enter all fields
                                For a partial modification, the PATCH action is available

        - DELETE http://127.0.0.1:8000/status_contract/{status_contract_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Delete the status contract object only if no contract are linked        

    EVENT

        - GET: http://127.0.0.1:8000/event/

            Authentication required
            Commercial access:  Returns the list of events to which the commercial is linked
            Support Access:     Returns the list of events to which the support is linked
            Admin access :      Returns the list of events

        - GET: http://127.0.0.1:8000/event/{event_id}/

            Authentication required
            Commercial access:  Returns the event informations if the commercial user is linked
            Support Access:     Returns the event informations if the support user is linked
            Admin access :      Returns the event informations

        - POST http://127.0.0.1:8000/event/

            Authentication required
            Commercial access:  Create a event with date, attendees, status id, contract id, support contact id, notes(optional)
            Support Access:     Not allowed
            Admin access :      Create a event with date, attendees, status id, contract id, support contact id, notes(optional)
        
        - PUT http://127.0.0.1:8000/event/{event_id}/

            Authentication required
            Commercial access:  Modify a event informations only if the commercial user is linked, the user must enter all fields
                                For a partial modification, the PATCH action is available
            Support Access:     Modify a event informations only if the support user is linked, the user must enter all fields
                                For a partial modification, the PATCH action is available
            Admin access :      Modify a event informations, the user must enter all fields
                                For a partial modification, the PATCH action is available
        
        - DELETE http://127.0.0.1:8000/contract/{contract_id}/

            Authentication required
            Commercial access:  Deletes the evnet object only if the commercial user is linked
            Support Access:     Not allowed
            Admin access :      Delete the event object only if no events are linked

    EVENT STATUS

        - GET: http://127.0.0.1:8000/status_event/

            Authentication required
            Commercial access:  Returns the list of status events
            Support Access:     Returns the list of status events
            Admin access :      Returns the list of status events

        - GET: http://127.0.0.1:8000/status_event/{status_event_id}

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Returns the status event informations

        - POST http://127.0.0.1:8000/status_event/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Create a status event with status name

        - PUT http://127.0.0.1:8000/status_event/{status_event_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Modify a status event informations, the user must enter all fields
                                For a partial modification, the PATCH action is available

        - DELETE http://127.0.0.1:8000/status_event/{status_event_id}/

            Authentication required
            Commercial access:  Not allowed
            Support Access:     Not allowed
            Admin access :      Delete the status event object only if no event are linked 
