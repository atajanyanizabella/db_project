#!/usr/bin/env python3

import psycopg2
from psycopg2 import sql

def initialize_db(db_name, owner_username, owner_password):
    # Connect to the default database to create a new DB
    connection = psycopg2.connect(
        dbname="postgres",
        user="admin",
        password="secret",
        host="localhost",
        port="5432"
    )

    # Set autocommit mode
    connection.autocommit = True

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    try:
        # Create a new DB
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

        # Connect to the newly created DB
        connection.close()
        connection = psycopg2.connect(
            dbname=db_name,
            user="admin",
            password="secret",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Commit the changes
        #connection.commit()

        print(f"Database '{db_name}' created and owned by '{owner_username}'.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    db_name = "ship_registry"
    owner_username = "admin"
    owner_password = "secret"

    initialize_db(db_name, owner_username, owner_password)
