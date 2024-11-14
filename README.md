# bookstore-project

This is the backend project of the bookstore application built with Django.

## Technology used

Python, Django, Django Rest Framework, Celery, RabbitMQ, Postgresql and Docker.

# Prerequisites

1. To run this project you need to install docker on your system.

# Installation

1. Clone the repository:
2. Change directory to django-video-streaming-project by running `cd bookstore_project`
3. Set up following environment variables:

```
ENVIRONMENT=development
SECRET_KEY=lu)x9450)n4#5DIkx)d3zgbbv5ifnikqtjdg%i0lld5ki7*$5em!f)
DEBUG=1

DB_NAME=bookstore_db
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=host.docker.internal
DB_PORT=5432

RABBITMQ_HOST=host.docker.internal
RABBITMQ_PORT=5673
RABBITMQ_USER=guest
RABBITMQ_PASSWORD=guest

```

Create a .env file in the root directory and provide the required values for environment variables such as database
credentials.

# Build Docker containers:

To run this project you just need to run the following command and the rest will do itself.

`docker compose up --build`

This command will build and start the Docker containers required for the project.

# Admin Interface:

The admin panel can be accessed at http://localhost:8000/admin/
But you need to create a superuser account first.
