import os # to access operating system  I use this to access the .env file configuration
import psycopg # import driver to communicate python and postgresql server

from dotenv import load_dotenv # import and load the configuration in .env file
load_dotenv()


connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

print("Connected!")

cursor = connection.cursor() # create executor for CRUD

# CREATE TABLE using cursor executor
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(255) NOT NULL
    );
"""
)

# INSERT Data into table
cursor.execute(
    """
    Insert INTO users (name, email)
    """,
    ("chad","sample@gmail.com")    
)

# SAVE and make permanent of changes on current transaction
connection.commit()

# CANCEL the transaction changes
# connection.rollback()


# READ/Access Data stored in table
cursor.execute("SELECT id, name, email FROM users;")

# Result using fetchall
users = cursor.fetchall()

# PRINT the result of fetchall
for user in users:
    print(user)

