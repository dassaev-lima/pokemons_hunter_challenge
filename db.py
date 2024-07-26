import sqlite3

def search_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    
    return results

username = input("Enter username: ")
print(search_user(username))
