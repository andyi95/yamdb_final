en | [ru](README.md)

# Yamdb API
## Description

[![Yamdb app workflow](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=master)](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml)

**YAMDB** is an online service, collecting user's reviews for different compositions divided into different categories and genres. There're a few pre-installed set of categories and genres but you may add some custom ones.
The project is built from repo [andyi95/api_yamdb](https://github.com/andyi95/api_yamdb) with CI/CD [GitHubActions](https://github.com/features/actions), Docker and Docker-compose toolset.

Tech stack used in this project: Python3, Django Rest Framework, PostgreSQL, Gunicorn, Docker

## Demo server

A server with deployed and running project can be found by the following URL http://yatube.blackberrystudio.com/. You can read the API online docs [here](http://yatube.blackberrystudio.com/redoc).

## Build and deploy

#### Docker and Docker-compose packages installation
*Applicable for Ubuntu distros, for other operation systems consult the relevant [Docker docs section](https://docs.docker.com/get-docker/)*

```shell
# Installation of packages used for adding a side-channel Docker repositories
sudo apt update
sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y
# Import Docker GPG keys and add the repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
# Docker packages download and install
sudo apt install docker-ce docker-compose -y
```
Restart the server and check if Docker installation passed correctly with following commands: `service docker status` and `docker ps -a`.
 
#### Clone repository

Attention! Check that neither PostgreSQL, nor any web-services are running on your host before the deployment, otherwise check the Docker port mapping [guides](https://docs.docker.com/config/containers/container-networking/).

For the proper deployment you need to clone repository, copy `docker-compose.yaml` to the home directory and add following Action Secret keys in repository settings:
  - `SECRET_KEY` - 20-symbols Django key used for generating cookies, crsf and save storages
  - `DB_HOST`, `DB_PORT`  - PostgreSQL server container's hostname and port. If necessary, you may use PostgreSQL server running on the host - for appropriate network configuration check the [docs section](https://docs.docker.com/compose/networking/) dedicated to port mapping between containers and host.
  - `DB_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD` - database name, PostgreSQL username and password used for save connection.
  - `HOST`, `USER`, `SSH_KEY`/`PASSWORD`, `PASSPHRASE` - network address, username, private SSH-key (with a passphrase if used) or password, used for SSH deployment. Check the official [ssh-action](https://github.com/appleboy/ssh-action) repo for more parameters. 
  - `TELEGRAM_TOKEN`, `TELEGRAM_TO` - Telegram bot's token and user id for sending notifications. Check the [Telegram manuals](https://core.telegram.org/bots#6-botfather) to know more about Telegram bots creation and management.

In future you may edit the `~/.env` file according to your current requirements as the existing fields are not overwritten with the new deployments.

#### Initial configs

After the tests and deploy have been completed, the initial configurations might be proceeded:
```shell
docker-compose exec web bash
python manage.py migrate
python manage.py collectstatic --no-input
exit
```
The script above indexes static files and set up database fields and relations. Also, a superuser account for admin panel management might be useful:

```shell
docker exec web python manage.py createsuperuser
```

#### Common usage and administration

After the containers installation you may consult the Yamdb API documentation by the following address http://localhost/redoc/ (`localhost`) should be replaced on the actual server address.

The Django admin panel is placed by URL http://localhost/admin/
  
#### Initial dataset usage

The site is bundled with a test set of data, which may be installed by the command
```shell
docker exec web python manage.py loaddata fixtures.json
```

#### Stop and remove containers

``shell
docker-compose stop
docker-compose rm web
``
 
 Keep in mind, that after the main worker container's removal, the database and some of config files stays in *Docker volumes*. Run the following command for complete removal of all the rest data: `docker volume prune`
 
#### Potential problems

- In some cases any Docker commands result an error docker: `Got permission denied while trying to connect to the Docker daemon socket at...` and Docker runs correctly only with superuser privileges. To fix the error and allow Docker to launch with rights of current user you shall create `docker` group and add the current user to it:
```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```
Then you have to terminate current session and login under the current user again to apply the changes (sometimes you may have also to reboot the host).
 
## Authors

This project was developed by:

 - [andyi95](https://github.com/andyi95)
 - [Dkobachevski](https://github.com/dmarichuk)
 - [dmarichuk](https://github.com/dmarichuk)


## Tools and frameworks
 
 - [Python 3.x](https://www.python.org/) | [docs](https://docs.python.org/3/) | [GitHub](https://github.com/python/cpython/tree/3.8)
 - [Django 3.1.x](https://www.djangoproject.com/) [docs](https://docs.djangoproject.com/en/3.1/) | [GitHub](https://github.com/django/django/tree/stable/3.1.x)
 - [Gunicorn](https://gunicorn.org/) | [Github](https://github.com/benoitc/gunicorn)
 - [PostgreSQL 12](https://www.postgresql.org/) | [docs](https://www.postgresql.org/docs/12/index.html) | [GitHub](https://github.com/postgres/postgres/tree/REL_12_STABLE)
 - [Nginx HTTP Server](https://nginx.org/ru/) | [docs](https://nginx.org/ru/docs/) | [GitHub](https://github.com/nginx/nginx/tree/branches/stable-1.12)
 - [Docker](https://docs.docker.com/) | [Github](https://github.com/docker)
 - [Docker Compose](https://docs.docker.com/compose/) | [Github](https://github.com/docker/compose)
 - [GitHub Actions](https://github.com/features/actions) | [docs](https://github.com/features/actions)