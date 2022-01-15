# Wagtail-tailwind-starter

This is a generated build of Wagtail 2.15 and Tailwind 3.0 to help get started with a pre-configured build.

## Getting started
To run this project at is base you only need docker-compose installed and to run:
```
docker-compose up -d && docker-compose exec web /bin/bash 
```
Then in the web container you can run the django development server with:
```
./manage.py runserver 0:8000
```

To run and develop the front end you will need to install the packages with:
```
npm install 
```
and then run the development tooling with:
```
npm run start
```

## Advanced usage
In this project I use poetry as my virtual environment so you will need to install it locally follow the guide [here](https://python-poetry.org/docs/) for setup. Once you've created a virtual env and accessed it with ```poetry shell``` you can now use the fabric commands in the build.

Please note that the fab file will need to configured for your project, it includes commands to pull databases from staging and production Heroku environments as well as AWS S3 for media files.


fab commands: 
```
  build                    Build the development environment (callthisfirst)

  destroy                  Destroy development environment containers(database will be lost!)
  
  heroku-login             Log into the Heroku app for accessing config vars,  database backups etc.
  import-data              Import local data file to the db container .
  
  production-shell         Spin up a one-time Heroku production dyno and connect to shell
  
  psql                     Connect to the local postgres DB using psql
  
  pull-production-data     Pull database from production Heroku Postgres
  
  pull-production-images   Pull images from production AWS S3
  
  pull-production-media    Pull media from production AWS S3
  
  pull-staging-data        Pull database from staging Heroku Postgres
  
  pull-staging-images      Pull images from staging AWS S3
  
  pull-staging-media       Pull media from staging AWS S3
  
  push-staging-media       Push local media  content to staging instance
  
  restart                  Restart the  development  environment
  
  ssh                      Run bash in the local web container
  
  ssh-root                 Run bash as root in the local web container
  
  staging-shell            Spin up a one- time Heroku staging dyno and connect to shell
  
  start                    Start the development environment

  stop                     Stop the development environment
```