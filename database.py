import sqlite3
import json
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # جدول حفظ نتائج وإجابات الطلاب
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        full_name TEXT,
        username TEXT,
        answers TEXT,
        scores TEXT,
        top_majors TEXT,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_user_result(user_id, full_name, username, answers, scores, top_majors):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO users (user_id, full_name, username, answers, scores, top_majors, completed_at)
    VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (
        user_id,
        full_name,
        username,
        json.dumps(answers),
        json.dumps(scores),
        json.dumps(top_majors, ensure_ascii=False)
    ))
    conn.commit()
    conn.close()

def get_user_result(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT scores, top_majors, completed_at FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "scores": json.loads(row[0]),
            "top_majors": json.loads(row[1]),
            "completed_at": row[2]
        }
    return None
