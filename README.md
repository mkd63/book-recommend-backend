# My Books Backend

## About
A server side API which functions for my books application to maintain users, books and ratings mapped user to book to recommend books using collaborative filtering built on django.

## Built on Django
![django_rest_framework](https://ksr-ugc.imgix.net/assets/011/705/984/4ea78430d3ad7dc88106a7b973248ba7_original.jpg?ixlib=rb-2.1.0&crop=faces&w=1552&h=873&fit=crop&v=1463687041&auto=format&frame=1&q=92&s=022bf4c5b7efa27ab20395c0da4eff7b)

## Usage
To run the API locally:
1.	Setup a virtualenv and activate it.
2.	Install the packages as listed in the requirements.txt by running pip install. (Make sure you are in the virtual environment while doing this)
3.	The API uses some config variables to run in appropriate environments. Create a .env file and list the following variables:
  ```
  SECRET_KEY=DJANGO_GENERATED_SECRET_KEY
  DEBUG=True
  DATABASE_URL= postgres password
  ALLOWED_HOST=127.0.0.1
  DOMAIN=my-books-recommender.herokuapp.com
  GMAIL_USERNAME=sharmaaahan15@gmail.com
  GMAIL_PASSWORD=rzefymaglgycyute
  CLOUDINARY_API_KEY=YOUR_CLOUDINARY_API_KEY
  CLOUDINARY_CLOUD_NAME=CLOUDINARY_CLOUD_NAME
  CLOUDINARY_SECRET_KEY=CLOUDINARY_SECRET_KEY
  
  ```
## PostgreSQL 
PostgreSQL relational database has been used to store and manage the data. 

### Setup
1.	Make sure you have Postgres installed and create a database named my_books_development.
2.	Edit the DATABASE_URL in .env file and change it to your Postgres password.
3.	Go to your API directory and run python manage.py makemigrations to create the migration files for tables to created in the database from Django.
4.	Run python manage.py migrate to run the migration files and apply changes in PostgreSQL.
5.	Then finally, run python manage.py runserver to run the Django API server.


### Contributors

| Part           | Contributor                                   |
| :------------- | :-------------------------------------------- |
| Models and API | [Aahan Sharma](https://github.com/mkd63) |
| Postgres       | [Aahan Sharma](https://github.com/mkd63) |

