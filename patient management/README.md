# patient-management
# Basic project structure 
models/ - data base models
views/ - routes and view function
web_app/templates/ - html template files
web_app/static/ - css and js files
config.py - database credentials
auth/ - authencation decorater

# Cretaing virtual env and installing packages
    $ virtualenv env
    
    $ source env/bin/activate(linux)

    $ .\env\Scripts\activate(windows)

    $ pip install -r requirements.txt
        
# Running application
    $ python serve.py
    $ http://localhost:8080/login(user name and passowrd be anything)
