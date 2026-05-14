# Contacts REST API

A REST API application for storing and managing contacts built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **Alembic**.

The project supports full CRUD functionality, contact search, birthday reminders, automatic API documentation, and asynchronous database operations.

## Technologies Used

- Python 3.13
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- AsyncPG
- Pydantic
- Uvicorn
- Docker

# Project Structure

goit-pythonweb-hw-08/
│
├── migrations/
│
├── src/
│   ├── api/
|   |   ├── utils.py
│   │   └── contacts.py
│   │
│   ├── conf/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── models.py
│   │
│   ├── repository/
│   │   └── contacts.py
│   │
│   ├── services/
│   │   └── contacts.py
│   │
│   └── schemas.py
│
├── alembic.ini
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md

## The API supports:

- Create a contact
- Get all contacts
- Get contact by ID
- Update contact
- Delete contact
- Search contacts by:
- first name
- last name
- email
- Get upcoming birthdays for the next 7 days
- Swagger API documentation

### Swagger Documentation

![Swagger Docs](screenshots/swagger.png)

## Installation

### 1. Clone repository

git clone https://github.com/YOUR_USERNAME/goit-pythonweb-hw-08.git

### 2. Open project folder

cd goit-pythonweb-hw-08

### 3. Install dependencies

poetry install
poetry shell

## PostgreSQL Setup with Docker

### Run PostgreSQL container

docker run --name contacts-db \
-p 5432:5432 \
-e POSTGRES_PASSWORD=567234 \
-d postgres

### Create database inside container

docker exec -it contacts-db psql -U postgres

Create database:
CREATE DATABASE contacts_db;

## Database Configuration

File: 
src/conf/config.py

Code: 

class Config:
    DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/contacts_db"

config = Config()

## Alembic Migrations

alembic revision --autogenerate -m "Init"

### Apply migrations

alembic upgrade head

## Run Application

python main.py 
or
uvicorn main:app --reload 

Application runs on: http://127.0.0.1:8000

## Swagger Documentation and Testing

http://127.0.0.1:8000/docs

First I created two contacts: one with current date (of my work on project) and one with a few days later. 

![Get Contacts](screenshots/post_contacts.png)

Second step was checking if api works correctly and shows all endpoints in the right way. I link some of examples below.

See all contacts (by /api/contacts route):

![Search Contacts](screenshots/search_contacts.png)

Search of the contact by name (/api/contacts/search/?query=anna):

![Search Contact](screenshots/search_contact.png)

And show contacts by upcoming birthday (/api/contacts/birthdays):

![Birthdays](screenshots/birthdays.png)

## Validation

The project uses Pydantic for request and response validation.

Example:

- Valid email format required
- Birthday must be a valid date
- Required fields cannot be empty

## Asynchronous Support

The application uses:

- async SQLAlchemy engine
- async PostgreSQL driver (asyncpg)
- asynchronous FastAPI endpoints

This improves performance and scalability.