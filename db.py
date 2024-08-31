import sqlite3

def search_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Código corrigido com parametrização de consulta
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

# Exemplo de uso
username = input("Enter username: ")
print(search_user(username))
