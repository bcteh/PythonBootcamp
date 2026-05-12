import sqlite3
from datetime import datetime
from typing import List, Optional, Tuple


def parse_timestamp(ts):
    """Convert SQLite timestamp string to datetime."""
    if ts is None or isinstance(ts, datetime):
        return ts
    if isinstance(ts, str):
        # SQLite stores as "2026-05-12 14:30:45", convert to ISO format
        return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    return ts


class Databasemanager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Initialize the database and create tables if they don't exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                loginid TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user(self, loginid: str, name: str, age: int, email: str) -> None:
        """Create a new user."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO users (loginid, name, age, email)
                VALUES (?, ?, ?, ?)
            ''', (loginid, name, age, email))
            conn.commit()
        except sqlite3.IntegrityError as e:
            conn.close()
            raise sqlite3.IntegrityError(f"User already exists: {str(e)}")
        finally:
            conn.close()
    
    def get_user_by_loginid(self, loginid: str) -> Optional[dict]:
        """Get a user by loginid."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE loginid = ?', (loginid,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            user = dict(row)
            user['created_at'] = parse_timestamp(user['created_at'])
            return user
        return None
    
    def get_all_users(self) -> List[dict]:
        """Get all users."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        conn.close()
        
        users = []
        for row in rows:
            user = dict(row)
            user['created_at'] = parse_timestamp(user['created_at'])
            users.append(user)
        return users
    
    def update_user(self, loginid: str, name: Optional[str] = None, age: Optional[int] = None, email: Optional[str] = None) -> None:
        """Update a user."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE loginid = ?', (loginid,))
        if not cursor.fetchone():
            conn.close()
            raise ValueError(f"User with loginid '{loginid}' not found.")
        
        # Build update query
        updates = []
        params = []
        
        if name is not None:
            updates.append('name = ?')
            params.append(name)
        if age is not None:
            updates.append('age = ?')
            params.append(age)
        if email is not None:
            updates.append('email = ?')
            params.append(email)
        
        if updates:
            query = f"UPDATE users SET {', '.join(updates)} WHERE loginid = ?"
            params.append(loginid)
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    def delete_user(self, loginid: str) -> None:
        """Delete a user."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE loginid = ?', (loginid,))
        if not cursor.fetchone():
            conn.close()
            raise ValueError(f"User with loginid '{loginid}' not found.")
        
        cursor.execute('DELETE FROM users WHERE loginid = ?', (loginid,))
        conn.commit()
        conn.close()
