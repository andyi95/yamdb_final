# Yamdb API Final
[![Yamdb app workflow](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=master)](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml)
## Описание

**YAMDB** собирает отзывы пользователей на произведения, делящиеся на произвольные  категории и жанры, которые можно добавлять самостоятельно.
Оригинальный репозиторий проекта [andyi95/api_yamdb](https://github.com/andyi95/api_yamdb). Текущая версия проекта написана с поддержкой CI/CD инструментария [GitHub Actions](https://github.com/features/actions), Docker и Docker Compose. При создании использовался следующий стек технологий: Python3, Django Rest Framework, PostgreSQL, Gunicorn, Docker.

## Сборка и запуск проекта

#### Клонирование репозитория

Для корректного развертывания необходимо склонировать репозиторий, скопировать файл `docker-compose.yaml` в домашний каталог пользователя, от имени которого производится запуск контейнеров и заполнить поля с данными конфигурирования и удалённого сервера при помощи раздела Secrets в настройках склонированного репозитория GitHub. Для корректной работы используются следующие параметры:
 - `SECRET_KEY` - 20-и значный секретный ключ Django, использующийся для хранения cookie-сессий, генерации crsf-токенов и другой приватной информации. 
 - `DB_HOST`, `DB_PORT`  - имя контейнера и порт контейнера PostgreSQL сервера. При необходимости, возможна работа с PostgreSQL хост-машины, для конфигурации см. соответствующий [раздел](https://docs.docker.com/compose/networking/), посвященный настройке сети контейнеров.
  - `DB_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD` - название базы данных, имя пользователя и пароль соответственно.
  - `HOST`, `USER`, `SSH_KEY`/`PASSWORD`, `PASSPHRASE` - адрес, имя пользователя и закрытый SSH-ключ (с парольной фразой при защите ключа) либо пароль, использующийся для подключения к удалённому серверу. Подробнее о параметрах развертывания по SSH можно узнать из репозитория [ssh-action](https://github.com/appleboy/ssh-action)
  - `TELEGRAM_TOKEN`, `TELEGRAM_TO` - токен бота и id получателя для отправки Telegram-уведомлений. Инструкцию по созданию бота и получению необходимой информации можно из [докуменации Telegram](https://core.telegram.org/bots#6-botfather)
  
  
#### Первичная конфигурация

После успешного прохождения автоматических тестов и развёртывания, можно провести первичную настройку.
```shell
docker-compose exec web bash
python manage.py migrate
python manage.py collectstatic --no-input
exit
```
Данный скрипт выполнит индексацию статических файлов и настройку полей и связей базы данных.

#### Использование и администрирование

После установки и запуска контейнеров вы можете ознакомиться с документацией Yamdb API по следующему URL: http://localhost/redoc/ (localhost замените на адрес удаленного сервера, на котором происходила установка).

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
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker system prune
```
Необходимо учесть, что база данных и некоторые конфигурационные файлы остаются в *томах docker*. Для полного удаления всей оставшейся информации выполните команду `docker volume prune`

### Конфигурация .env файла
 
 Скопируйте или переименуйте `.env.sample` в `.env`.
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
 
 ## Инструменты и фреймворки в проекте
 
 - [Python 3.x](https://www.python.org/) | [docs](https://docs.python.org/3/) | [GitHub](https://github.com/python/cpython/tree/3.8)
 - [Django 3.1.x](https://www.djangoproject.com/) [docs](https://docs.djangoproject.com/en/3.1/) | [GitHub](https://github.com/django/django/tree/stable/3.1.x)
 - [Gunicorn](https://gunicorn.org/) | [Github](https://github.com/benoitc/gunicorn)
 - [PostgreSQL 12](https://www.postgresql.org/) | [docs](https://www.postgresql.org/docs/12/index.html) | [GitHub](https://github.com/postgres/postgres/tree/REL_12_STABLE)
 - [Nginx HTTP Server](https://nginx.org/ru/) | [docs](https://nginx.org/ru/docs/) | [GitHub](https://github.com/nginx/nginx/tree/branches/stable-1.12)
 - [Docker](https://docs.docker.com/) | [Github](https://github.com/docker)
 - [Docker Compose](https://docs.docker.com/compose/) | [Github](https://github.com/docker/compose)
 
