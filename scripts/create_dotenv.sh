#!/usr/bin/bash
echo "DB_NAME=$DB_NAME" > .env
echo "DB_HOST=$DB_HOST" >> .env
echo "DB_PORT=$DB_PORT" >> .env
echo "DB_USER=$DB_USER" >> .env
echo "DB_PASSWORD=$DB_PASSWORD" >> .env
echo "SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL" >> .env