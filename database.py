import sqlite3
from datetime import datetime
import os

DB_PATH = "data/employee.db"

def init_database():
    """Initialize SQLite database with required tables"""
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            joining_date TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Emotion logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emotion_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            emotion TEXT NOT NULL,
            face_score REAL,
            voice_score REAL,
            text_score REAL,
            adaptability_score REAL,
            retention_risk TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')
    
    # Feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            feedback_text TEXT NOT NULL,
            sentiment TEXT,
            sentiment_score REAL,
            stress_level TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')
    
    # Voice logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voice_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            transcript TEXT,
            sentiment TEXT,
            sentiment_score REAL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')
    
    # HR recommendations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            recommendation_text TEXT,
            priority TEXT,
            is_resolved BOOLEAN DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def add_employee(name, department, joining_date, email):
    """Add a new employee"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, department, joining_date, email)
        VALUES (?, ?, ?, ?)
    ''', (name, department, joining_date, email))
    conn.commit()
    employee_id = cursor.lastrowid
    conn.close()
    return employee_id

def get_employees():
    """Get all employees"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, department, joining_date, email FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def save_emotion_log(employee_id, emotion, face_score, voice_score, text_score, adaptability_score, retention_risk):
    """Save emotion analysis results"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO emotion_logs (employee_id, emotion, face_score, voice_score, text_score, adaptability_score, retention_risk)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (employee_id, emotion, face_score, voice_score, text_score, adaptability_score, retention_risk))
    conn.commit()
    conn.close()

def save_feedback(employee_id, feedback_text, sentiment, sentiment_score, stress_level):
    """Save employee feedback"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (employee_id, feedback_text, sentiment, sentiment_score, stress_level)
        VALUES (?, ?, ?, ?, ?)
    ''', (employee_id, feedback_text, sentiment, sentiment_score, stress_level))
    conn.commit()
    conn.close()

def save_voice_log(employee_id, transcript, sentiment, sentiment_score):
    """Save voice analysis results"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO voice_logs (employee_id, transcript, sentiment, sentiment_score)
        VALUES (?, ?, ?, ?)
    ''', (employee_id, transcript, sentiment, sentiment_score))
    conn.commit()
    conn.close()

def save_recommendation(employee_id, recommendation_text, priority):
    """Save HR recommendation"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO recommendations (employee_id, recommendation_text, priority)
        VALUES (?, ?, ?)
    ''', (employee_id, recommendation_text, priority))
    conn.commit()
    conn.close()

def get_employee_analytics(employee_id):
    """Get all analytics for an employee"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get emotion history
    cursor.execute('''
        SELECT timestamp, emotion, adaptability_score, retention_risk 
        FROM emotion_logs 
        WHERE employee_id = ? 
        ORDER BY timestamp DESC LIMIT 30
    ''', (employee_id,))
    emotion_history = cursor.fetchall()
    
    # Get feedback history
    cursor.execute('''
        SELECT timestamp, sentiment, stress_level 
        FROM feedback 
        WHERE employee_id = ? 
        ORDER BY timestamp DESC LIMIT 10
    ''', (employee_id,))
    feedback_history = cursor.fetchall()
    
    # Get recommendations
    cursor.execute('''
        SELECT recommendation_text, priority, is_resolved, created_at 
        FROM recommendations 
        WHERE employee_id = ? 
        ORDER BY created_at DESC
    ''', (employee_id,))
    recommendations = cursor.fetchall()
    
    conn.close()
    return emotion_history, feedback_history, recommendations

def get_all_employees_analytics():
    """Get aggregated analytics for all employees"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get latest emotion for each employee
    cursor.execute('''
        SELECT e.id, e.name, e.department, el.emotion, el.adaptability_score, el.retention_risk, el.timestamp
        FROM employees e
        LEFT JOIN emotion_logs el ON e.id = el.employee_id
        WHERE el.timestamp = (
            SELECT MAX(timestamp) FROM emotion_logs WHERE employee_id = e.id
        ) OR el.timestamp IS NULL
    ''')
    latest_status = cursor.fetchall()
    
    # Get risk distribution
    cursor.execute('''
        SELECT retention_risk, COUNT(*) 
        FROM emotion_logs 
        WHERE timestamp = (SELECT MAX(timestamp) FROM emotion_logs)
        GROUP BY retention_risk
    ''')
    risk_distribution = cursor.fetchall()
    
    conn.close()
    return latest_status, risk_distribution

def get_employee_by_id(employee_id):
    """Get employee details by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, department, joining_date, email FROM employees WHERE id = ?', (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    return employee