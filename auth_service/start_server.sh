#!/bin/sh

echo "Waiting for MySQL..."
# Wait for MySQL using netcat
while ! nc -z "$MYSQL_HOST" 3306; do
  sleep 1
done

echo "MySQL started"

uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
