## Librato Chart Sender Web

It's meant so that admins can acess the website and work with their own configurations and will load the librato chart sender app


# Usage

### Install instructions
1. Install Django

    * ```sudo pip install django```

2. Install django-fontawesome

    * ```sudo pip install django-fontawesome```

3. Install postgres package

	* install [postgress.app](http://postgresapp.com/)	

	* ```sudo pip install psycopg2```

	Configure your db via postgres console if needed:
	
	1. ```sudo su ```
	2. ```su postgres -c psql postgres```
	3. ```CREATE USER postgres WITH PASSWORD 'swat';```
	4. ```CREATE DATABASE librato_chart_sender WITH OWNER postgres;```
	5. ```GRANT ALL PRIVILEGES ON DATABASE librato_chart_sender TO postgres;```
	
    
4. Migrate the database to your machine

    * ```python manage.py migrate```

4. Run local server

    * ```python manage.py runserver``` 

5. Open webpage

    * http://localhost:8000
    
### Acess admin page

1. Create a superuser

    * ```python manage.py createsuperuser```
    
    It will ask for a username, email and password
    
2. Go to webpage

    * http://localhost:8000/admin
    
    And sign in with your account

