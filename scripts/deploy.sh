#!/bin/bash
# Deployment script - run on server or via CI
# DSCC 00015829 - Task Manager
set -e
cd "$(dirname "$0")/.."
export DOCKERHUB_USERNAME=${DOCKERHUB_USERNAME:-00015829}
echo "Pulling latest images..."
docker compose pull web
echo "Stopping old containers..."
docker compose down
echo "Starting new containers..."
docker compose up -d
echo "Running migrations..."
docker compose exec -T web python manage.py migrate --noinput
echo "Collecting static files..."
docker compose exec -T web python manage.py collectstatic --noinput
echo "Deployment complete."
