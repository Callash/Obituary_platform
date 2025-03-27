import psycopg2
from psycopg2 import sql
from datetime import datetime

def submit_obituary(name, date_of_birth, date_of_death, content, author, slug):
    # Database connection parameters
    db_params = {
        'dbname': 'obituary_db',
        'user': 'your_postgres_user',
        'password': 'your_postgres_password',
        'host': 'localhost',
        'port': '5432'
    }

    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Insert captured data into the obituaries table
        insert_query = sql.SQL("""
            INSERT INTO obituaries (Name, Date_of_birth, Date_of_death, Content, Author, Submission_date, Slug)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """)
        submission_date = datetime.now()

        cursor.execute(insert_query, (name, date_of_birth, date_of_death, content, author, submission_date, slug))
        conn.commit()

        # Provide a confirmation message to the user upon successful submission
        print("Obituary submitted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Example usage of the function
if __name__ == "__main__":
    name = "John Doe"
    date_of_birth = "1950-01-01"
    date_of_death = "2025-03-25"
    content = "John Doe was a beloved husband and father. He will be greatly missed."
    author = "Jane Doe"
    slug = "john-doe-obituary"
    
    submit_obituary(name, date_of_birth, date_of_death, content, author, slug)
