#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

celery -A bookstoreproject worker --loglevel=info