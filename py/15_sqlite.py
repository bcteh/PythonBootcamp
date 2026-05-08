import sqlite3
# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
# Create a class to interact with the database
class Database:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             age INTEGER,
                             email TEXT UNIQUE NOT NULL,
                             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    def create_post_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             user_id INTEGER,
                             title TEXT NOT NULL,
                             content TEXT,
                             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                             FOREIGN KEY(user_id) REFERENCES users(id))''')
        self.conn.commit()  

    def insert_user(self, name, age, email):
        self.cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))
        self.conn.commit()
    def get_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
    def update_user(self, user_id, name=None, age=None, email=None):
        fields = []
        values = []
        if name:
            fields.append('name = ?')
            values.append(name)
        if age:
            fields.append('age = ?')
            values.append(age)
        if email:
            fields.append('email = ?')
            values.append(email)
        values.append(user_id)
        self.cursor.execute(f'UPDATE users SET {", ".join(fields)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?', values)
        self.conn.commit()
    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
    def insert_post(self, user_id, title, content):
        self.cursor.execute('INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)', (user_id, title, content))
        self.conn.commit()
    def get_posts(self):
        self.cursor.execute('SELECT * FROM posts')
        return self.cursor.fetchall()
    def update_post(self, post_id, title=None, content=None):
        fields = []
        values = []
        if title:
            fields.append('title = ?')
            values.append(title)
        if content:
            fields.append('content = ?')
            values.append(content)
        values.append(post_id)
        self.cursor.execute(f'UPDATE posts SET {", ".join(fields)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?', values)
        self.conn.commit()
    def delete_post(self, post_id):
        self.cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        self.conn.commit()
    
    def display_menu(self):
        print("1. Create User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Create Post")
        print("6. View Posts")
        print("7. Update Post")
        print("8. Delete Post")
        print("9. Exit")
# Create an instance of the Database class and create tables
db = Database(conn)
db.create_table()
db.create_post_table()
# Main loop to display the menu and handle user input
while True:
    db.display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        db.insert_user(name, age, email)
    elif choice == '2':
        users = db.get_users()
        for user in users:
            print(user)
    elif choice == '3':
        user_id = int(input("Enter user ID to update: "))
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        db.update_user(user_id, name if name else None, int(age) if age else None, email if email else None)
    elif choice == '4':
        user_id = int(input("Enter user ID to delete: "))
        db.delete_user(user_id)
    elif choice == '5':
        user_id = int(input("Enter user ID for the post: "))
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        db.insert_post(user_id, title, content)
    elif choice == '6':
        posts = db.get_posts()
        for post in posts:
            print(post)
    elif choice == '7':
        post_id = int(input("Enter post ID to update: "))
        title = input("Enter new title (leave blank to keep current): ")
        content = input("Enter new content (leave blank to keep current): ")
        db.update_post(post_id, title if title else None, content if content else None)
    elif choice == '8':
        post_id = int(input("Enter post ID to delete: "))
        db.delete_post(post_id)
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")
# Close the database connection when done
conn.close()    


