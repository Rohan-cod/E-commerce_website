# E-commerce_website
An E-commerce website made using the Django framework.

## Major Contributors
  * [@Rohan-cod](https://github.com/Rohan-cod)
  * [@shubhdeeprajput](https://github.com/shubhdeeprajput)


## Requirements

Python 3.7  
Django 2.2.8  
And additional requirements are in **Pipfile**.

## Setting up the Project

  * Download and install Python 3.7
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/E-commerce_website.git`
  * Change directory to E-commerce_website `$ cd E-commerce_website`
  * Install pipenv `$ pip3 install pipenv`  
  * Create a virtual environment and install all requirements from Pipfile `$ pipenv install`  
  * Activate the env: `$ pipenv shell`
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create superuser `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`
  
## Deployment
The notes app has been deployed in production using heroku. Here's a list of steps to be followed for deploying an app to heroku:

  * Run pipenv lock to generate the appropriate Pipfile.lock `$ pipenv lock`
  * Then create a Procfile which tells Heroku how to run the remote server where our code will live. `$ touch Procfile`
  * For now we’re telling Heroku to use gunicorn as our production server and look in our mb_project.wsgi file for further instructions. `Update Procfile with - web: gunicorn <project_name>.wsgi --log-file - `
  * Next install [gunicorn](https://gunicorn.org) which we’ll use in production while still using Django’s internal server for local development use. `$ pipenv install gunicorn==19.9.0`
  * Finally update ALLOWED_HOSTS with '*' in settings.py file.
  * push the updates to the GitHub repository.
  * Login to heroku. `$ heroku login`
  * Create a new heroku app. `$ heroku create <app_name>`
  * Set git to use the name of your new app when you push to Heroku. `$ heroku git:remote -a <app_name>`
  * If there are no static files run `$ heroku config:set DISABLE_COLLECTSTATIC=1`
  * Push the code to Heroku. `$ git push heroku master`
  * Add free scaling so the app is actually running online. `$ heroku ps:scale web=1`
  

## Contributing

Feel free to raise a issue or make a pull request to fix a bug or add a new feature. If you are new to open source you can first read about git by [clicking here](https://www.codecademy.com/learn/learn-git).
