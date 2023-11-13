import sqlite3

class CRUD:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_name (
                id INTEGER PRIMARY KEY,
                column1 TEXT,
                column2 TEXT
            )
        """)
        self.conn.commit()

    def create(self, data):
        self.cursor.execute("INSERT INTO table_name (column1, column2) VALUES (?, ?)", data)
        self.conn.commit()

    def read(self, id):
        self.cursor.execute("SELECT * FROM table_name WHERE id=?", (id,))
        return self.cursor.fetchone()

    def update(self, id, data):
        self.cursor.execute("UPDATE table_name SET column1=?, column2=? WHERE id=?", (*data, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM table_name WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()