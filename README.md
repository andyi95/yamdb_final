[en](README-en.md) | ru

# Yamdb API Final
[![Yamdb app workflow](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=master)](https://github.com/andyi95/yamdb_final/actions/workflows/yamdb_workflow.yaml)
## Описание

**YAMDB** собирает отзывы пользователей на произведения, делящиеся на произвольные  категории и жанры, которые можно добавлять самостоятельно.
Оригинальный репозиторий проекта [andyi95/api_yamdb](https://github.com/andyi95/api_yamdb). Текущая версия проекта написана с поддержкой CI/CD инструментария [GitHub Actions](https://github.com/features/actions), Docker и Docker Compose. При создании использовался следующий стек технологий: Python3, Django Rest Framework, PostgreSQL, Gunicorn, Docker.

## Демо-страница проекта

С запущенным проектом можно ознакомиться по адресу http://yatube.blackberrystudio.com/
Документация проекта http://yatube.blackberrystudio.com/redoc/

## Сборка и запуск проекта

#### Установка Docker и Docker-compose

*Применимо для дистрибутов Ubuntu, для установки на других ОС см. соответствующий раздел [документации Docker](https://docs.docker.com/get-docker/)*

```shell
# Установка необходимых пакетов для добавления стороннего репозитория
sudo apt update
sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y
# Установка GPG ключа и самого резопитория Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
# Загрузка и установка пакетов Docker
sudo apt install docker-ce docker-compose -y
```
Выполните перезагрузку и проверьте корректную работу Docker командами `service docker status` и `docker ps -a`. 


#### Клонирование репозитория

Для корректного развертывания необходимо склонировать репозиторий, скопировать файл `docker-compose.yaml` в домашний каталог пользователя, от имени которого производится запуск контейнеров и заполнить поля с данными конфигурирования и удалённого сервера при помощи раздела Secrets в настройках склонированного репозитория GitHub. Для корректной работы используются следующие параметры:
 - `SECRET_KEY` - 20-и значный секретный ключ Django, использующийся для хранения cookie-сессий, генерации crsf-токенов и другой приватной информации. 
 - `DB_HOST`, `DB_PORT`  - имя контейнера и порт контейнера PostgreSQL сервера. При необходимости, возможна работа с PostgreSQL хост-машины, для конфигурации см. соответствующий [раздел](https://docs.docker.com/compose/networking/), посвященный настройке сети контейнеров.
  - `DB_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD` - название базы данных, имя пользователя и пароль соответственно.
  - `HOST`, `USER`, `SSH_KEY`/`PASSWORD`, `PASSPHRASE` - адрес, имя пользователя и закрытый SSH-ключ (с парольной фразой при защите ключа) либо пароль, использующийся для подключения к удалённому серверу. Подробнее о параметрах развертывания по SSH можно узнать из репозитория [ssh-action](https://github.com/appleboy/ssh-action)
  - `TELEGRAM_TOKEN`, `TELEGRAM_TO` - токен бота и id получателя для отправки Telegram-уведомлений. Инструкцию по созданию бота и получению необходимой информации можно из [докуменации Telegram](https://core.telegram.org/bots#6-botfather).
  
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
docker-compose stop
docker-compose rm web
```
Необходимо учесть, что база данных и некоторые конфигурационные файлы остаются в *томах docker*. Для полного удаления всей оставшейся информации выполните команду `docker volume prune`


#### Возможные проблемы

 - В некоторых случаях выполнение команд docker завершается ошибкой `docker: Got permission denied while trying to connect to the Docker daemon socket at...` - в таком случае необходимо создать группу `docker`  и добавить в неё текущего пользователя:
 ```shell
sudo groupadd docker
sudo usermod -aG docker $USER
 ```
После этого необходимо перезапустить сеанс текущего пользователя для применения изменений или перезапустить машину.

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
 - [GitHub Actions](https://github.com/features/actions) | [docs](https://github.com/features/actions)
 
