#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

su -m myuser -c "celery -A projectSlackBot beat --loglevel=info --scheduler=django_celery_beat.schedulers:DatabaseScheduler"