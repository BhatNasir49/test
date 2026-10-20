import sqlite3

def search_users(user_input):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # Critical Flaw: Unsanitized SQL query string formatting
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)

    return cursor.fetchall()

# trigger review
