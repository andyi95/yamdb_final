# Yamdb API
## Description

[![Yamdb app workflow](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=master)](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml)
**YAMDB** is an online service, collecting user's reviews for different compositions divided into different categories and genres. There're a few pre-installed set of categories and genres but you may add some custome ones.
The project is built from repo [andyi95/api_yamdb](https://github.com/andyi95/api_yamdb) with additional support of Docker and Docker Compose for deploy.

Tech stack used in this project: Python3, Django Rest Framework, PostgreSQL, Gunicorn, Docker

## Build and deploy

#### Docker and Docker-compose packages installation

 If you have installed Docker and Docker-compose before you may skip this step, otherwise you may use the official [docs](https://docs.docker.com/engine/install/) for the installation guidness.
 
#### Clone repository

Attention! Check that neither PostgreSQL, nor any web-services are running on your host before the deployment, otherwise check the Docker port mapping [guides](https://docs.docker.com/config/containers/container-networking/).

For the proper deployment you need to clone repository, copy `docker-compose.yaml` to the home directory and add following Action Secret keys in repository settings:
  - `SECRET_KEY` - 20-symbols Django key used for generating cookies, crsf and save storages
  - `DB_HOST`, `DB_PORT`  - PostgreSQL server container's hostname and port. If neccessary, you may use PostgreSQL server running on the host - for appropriate network configuration check the [docs section](https://docs.docker.com/compose/networking/) dedicated to port mapping between containers and host.
  - `DB_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD` - database name, PostgreSQL username and password used for save connection.
  - `HOST`, `USER`, `SSH_KEY`/`PASSWORD`, `PASSPHRASE` - network address, username, private SSH-key (with a passphrase if used) or password, used for SSH deployment. Check the offcial [ssh-action](https://github.com/appleboy/ssh-action) repo for more parameters. 
  - `TELEGRAM_TOKEN`, `TELEGRAM_TO` - Telegram bot's token and user id for sending notifications. Check the [Telegram manuals](https://core.telegram.org/bots#6-botfather) to know more about Telegram bots creation and management.

Furthermore, you may edit the `.env` file according to your current requirements as the existing fields are not overwritten with the new deployments.

#### Initial configs

After the tests and deploy have been completed, the initial configurations might be proceed:
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
  
#### Inital dataset usage

The site is bundled with a test set of data, which may be installed by the command
```shell
docker exec web python manage.py loaddata fixtures.json
```

#### Containers management
It's necessary to For the first run initialization 

Для запуска образа необходимо скопировать и заполнить отсутствующие поля своими значениями. Подробнее о конфигурации читайте в соответствующем [разделе](###конфигурация-.env-файла).

В файле `.env` содержатся основные параметры развёртывания - в целях безопасности рекомендуется заменить поля с секретным ключом Django, именем пользователя и паролем PostgreSQL (SECRET_KEY, POSTGRES_USER и POSTGRES_PASSWORD) на свои. Более подробно с рекомендациями по развертыванию Django можно ознакомиться по [ссылке](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/).

После копирования и заполнения env-файла начальными значениями, выполните сборку и запуск контейнеров:
```shell
git clone https://github.com/andyi95/infra_sp2
docker-compose up -d --build
docker-compose exec web bash

python manage.py migrate
python manage.py collectstatic --no-input
exit
```

#### 3. Использование и администрирование

После установки и запуска контейнеров вы можете ознакомиться с документацией по следующему URL: http://localhost/redoc/ (localhost замените на адрес удаленного сервера, на котором происходила установка).

Панель администрирования доступна по адресу http://localhost/admin/

##### Создание суперпользователя:

```shell
docker-compose exec web python manage.py createsuperuser
```
##### Заполнение БД тестовым набором данных

```shell
docker exec web python manage.py loaddata fixtures.json
```

##### Остановка и удаление контейнеров

```shell
docker-compose down
docker system prune
```

### Конфигурация .env файла
 
 Скопируйте скопируйте или переименуйте `.env.sample` в `.env`.
 Поле `SECRET_KEY` используется для поддержки cookie-сессий и crsf-токенов. Для генерации нового значения можно использовать команду (из контейнера `web`, либо иного окружения с установленным python и Django):
 ```shell
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
``` 
Полученное значение скопируйте в соответствующее поле.

Поле `POSTGRES_DB` содержит название базы данных, поля `POSTGRES_USER`, `POSTGRES_PASSWORD` - имя пользователя и пароль соответственно. По умолчанию в поле `DB_HOST` и `DB_PORT` используется база данных контейнера `db` с портом 5432, но так же можно использовать и PostgreSQL сервер хост-машины. Подробнее о настройке доступа к сервисам хоста из контейнеров описано в [документации Docker](https://docs.docker.com/compose/networking/).

Поле `HOSTS_LIST` определяет набор сетевых адресов, по которым будет производиться обращение к серверу (например, www.example.com, 109.210.52.211). Значение по умолчанию - "петлевой" адрес 127.0.0.1. Подробнее о назначении имён сервера можно узнать из [официальной документации Nginx](https://nginx.org/ru/docs/http/server_names.html)

## Авторы

Также над проектом работали: 
 - [andyi95](https://github.com/andyi95)
 - [Dkobachevski](https://github.com/dmarichuk)
 - [dmarichuk](https://github.com/dmarichuk)
