import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            phone VARCHAR(30) NOT NULL
        );
        """,
        """
        CREATE TABLE snake_user (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL DEFAULT 0,
            level INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES snake_user (user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()