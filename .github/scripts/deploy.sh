#!/bin/bash

docker-compose stop
docker-compose rm web
docker pull andyi95/yamdb_final
if ! grep -q "SECRET_KEY" .env ; then
  echo SECRET_KEY="${{ secrets.SECRET_KEY }}" > .env
fi
if ! grep -q "DB_ENGINE" .env ; then
  echo DB_ENGINE=${{ secrets.DB_ENGINE }} >> .env
fi
if ! grep -q "POSTGRES_DB" .env ; then
  echo POSTGRES_DB=${{ secrets.DB_NAME }} >> .env
fi
if ! grep -q "POSTGRES_USER" .env ; then
  echo POSTGRES_USER=${{ secrets.POSTGRES_USER }} >> .env
fi
if ! grep -q "POSTGRES_PASSWORD" .env ; then
  echo POSTGRES_PASSWORD=${{ secrets.POSTGRES_PASSWORD }} >> .env
fi
if ! grep -q "DB_HOST" .env ; then
  echo DB_HOST=${{ secrets.DB_HOST }} >> .env
fi
if ! grep -q "DB_PORT" .env ; then
  echo DB_PORT=${{ secrets.DB_PORT }} >> .env
fi
if ! grep -q "HOSTS_LIST" .env ; then
  echo HOSTS_LIST=${{ secrets.HOSTS_LIST }} >> .env
fi
if ! grep -q "DEBUG_MODE" .env ; then
  debug_mode=${{ secrets.DEBUG_MODE }}
fi
[[ "$debug_mode" == "TRUE" ]] && echo DEBUG_MODE=$debug_mode >> .env || echo "DEBUG_MODE=FALSE" >> .env
docker-compose up -d