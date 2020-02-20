## Fee Calculator ###
A simple web application that calculates a fee based on supplied amount.
Included in this app is a django rest api backend and a vanilla js frontend to demonstrate how to consume the api.

### Setup and Installation
- Create a virtual environment (python3.5 >):
```shell script
> virtualenv .venv
```
- Activate your environment
```shell script
> source .venv/bin/activate
```
- Install requirements
```shell script
> pip install requirements.txt
```

- Create a postgres database
```shell script
>psql

CREATE DATABASE <db_name>;
CREATE USER <db_user> WITH ENCRYPTED PASSWORD <db_password>;
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user>;
```

- Update the `calculator.env` file with the new database credentials.

- Run migration and start the app
```shell script
> python manage.py migrate
> python manage.py runserver
```