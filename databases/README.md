# PostgreSQL + Python

A practice project for learning how to configure PostgreSQL and connect it to Python using `psycopg`.

## Learning Goals

This project covers:

- PostgreSQL installation and configuration
- PostgreSQL users and roles
- Database creation
- Database permissions
- SQL basics
- Python ↔ PostgreSQL connection
- CRUD operations
- Transactions
- Environment variables

## Tech Stack

- Python
- PostgreSQL
- psycopg
- python-dotenv
- Git

## Project Structure

```text
postgres-python/
├── .gitignore
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd postgres-python
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install psycopg[binary] python-dotenv
```

## PostgreSQL Configuration

Create a PostgreSQL database:

```sql
CREATE DATABASE backend_db;
```

Create an application user:

```sql
CREATE USER app_user WITH PASSWORD 'your_password';
```

Grant access:

```sql
GRANT ALL PRIVILEGES ON DATABASE backend_db TO app_user;
```

## Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=backend_db
DB_USER=app_user
DB_PASSWORD=your_password
```

Do **not** commit `.env` to Git.

Use `.env.example` as a template.

## Run

Start the application:

```bash
python main.py
```

The application should connect to PostgreSQL and verify the connection.

## Database Architecture

```text
Python Application
       │
       ▼
    psycopg
       │
       ▼
PostgreSQL Server
       │
       ▼
   backend_db
       │
       ▼
    public
       │
       ▼
     tables
```

## Current Learning Progress

- [x] PostgreSQL installation
- [x] PostgreSQL service configuration
- [x] Create database
- [x] Create PostgreSQL user
- [x] Configure permissions
- [x] Python virtual environment
- [x] Install psycopg
- [x] Connect Python to PostgreSQL
- [x] Create tables
- [x] INSERT
- [x] SELECT
- [ ] UPDATE
- [ ] DELETE
- [ ] Transactions
- [ ] Relationships
- [ ] Indexes
- [ ] SQLAlchemy
- [ ] Alembic

## Security Notes

- Never commit `.env`.
- Do not use PostgreSQL superuser accounts for application connections.
- Use a dedicated database user for the application.
- Store credentials in environment variables or a proper secrets manager.
