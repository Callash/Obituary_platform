import psycopg2
from psycopg2 import sql
from flask import Flask, render_template_string

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'obituary_db',
    'user': 'your_postgres_user',
    'password': 'your_postgres_password',
    'host': 'localhost',
    'port': '5432'
}

# HTML template for displaying obituaries
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Obituaries</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Obituaries</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Date of Birth</th>
                <th>Date of Death</th>
                <th>Content</th>
                <th>Author</th>
                <th>Submission Date</th>
                <th>Slug</th>
            </tr>
        </thead>
        <tbody>
            {% for obituary in obituaries %}
            <tr>
                <td>{{ obituary[0] }}</td>
                <td>{{ obituary[1] }}</td>
                <td>{{ obituary[2] }}</td>
                <td>{{ obituary[3] }}</td>
                <td>{{ obituary[4] }}</td>
                <td>{{ obituary[5] }}</td>
                <td>{{ obituary[6] }}</td>
                <td>{{ obituary[7] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route('/view_obituaries')
def view_obituaries():
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # SQL query to select all records from the obituaries table
        select_query = "SELECT * FROM obituaries"
        cursor.execute(select_query)

        # Fetch all records
        obituaries = cursor.fetchall()

        # Render the HTML template with the retrieved data
        return render_template_string(html_template, obituaries=obituaries)

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
