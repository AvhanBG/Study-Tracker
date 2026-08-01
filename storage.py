import sqlite3

from datetime import datetime
from study_session import StudySession

print("storage.py imported")

class Storage:

    def __init__(self):
        print("Storage __init__ running")
        self.connection = sqlite3.connect("storage.db")
        self.create_table()


    def create_table(self):
        print("Creating table")
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            duration_minutes INTEGER NOT NULL
        )
        """)

        self.connection.commit()

    def save_session(self, session):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO sessions
        (date, start_time, end_time, duration_minutes)
        VALUES (?, ?, ?, ?)
        """,
        (
            str(session.date),
            str(session.start_time),
            str(session.end_time),
            str(session.duration_minutes)
        ))

        self.connection.commit()

    def load_sessions(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT * FROM sessions
        """)
        rows = cursor.fetchall()
        sessions = []
        for row in rows:
            session = StudySession(row[0])
            session.id = row[0]
            session.date = datetime.strptime(row[1], "%Y-%m-%d").date()
            session.start_time = row[2]
            session.end_time = row[3]
            session.duration_minutes = row[4]
            sessions.append(session)
        return sessions