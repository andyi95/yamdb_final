# Yamdb API Final
## Описание

**YAMDB** собирает отзывы пользователей на произведения, делящиеся на произвольные  категории и жанры, которые можно добавлять самостоятельно.
Проект склонирован из репозитория [andyi95/infra_sp2](http://github.com/andyi95/infra_sp2)
Проект собран из репозитория [andyi95/api_yamdb](https://github.com/andyi95/api_yamdb) с добавлением поддержки Docker и Docker Compose. При создании использовался следующий стек технологий: Python3, Django Rest Framework, PostgreSQL, Gunicorn, Docker

## Сборка и запуск проекта

#### 1. Установка Docker и Docker-compose

 Если у вас уже установлены docker и docker-compose, этот шаг можно пропустить, иначе можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).
 
#### 2. Установка и запуск контейнеров

Внимание! Убедитесь, что на хост-машине не запущены серверы PostGreSQL и/или веб-сервисы, в ином случае перед развёртыванием ознакомьтесь с документацией Docker по сопоставлению портов (port mapping).

В файле `.env` содержатся основные параметры развёртывания - в целях безопасности рекомендуется заменить поля с секретным ключом Django, именем пользователя и паролем PostgreSQL (SECRET_KEY, POSTGRES_USER и POSTGRES_PASSWORD) на свои. Более подробно с рекомендациями по развертыванию Django можно ознакомиться по [ссылке](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/).

Для запуска образа необходимо скопировать и заполнить отсутствующие поля своими значениями. Подробнее о конфигурации читайте в соответствующем [разделе](#конфигурация-env-файла).

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

После установки и запуска контейнеров вы можете ознакомиться с документацией по использованию Yamdb API по следующему URL: http://localhost/redoc/ (localhost замените на адрес удаленного сервера, на котором происходила установка).

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
 
