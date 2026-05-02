
import sqlite3

DB_NAME = "money_exchange.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone_number TEXT,
        address TEXT
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        position TEXT,
        email TEXT UNIQUE,
        phone_number TEXT
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS currency (
        currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
        currency_name TEXT NOT NULL,
        currency_code TEXT UNIQUE,
        country TEXT,
        symbol TEXT
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exchange_rate (
        rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
        currency_id INTEGER,
        buying_rate REAL,
        selling_rate REAL,
        updated_date TEXT,
        status TEXT,
        FOREIGN KEY (currency_id) REFERENCES currency(currency_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        employee_id INTEGER,
        currency_id INTEGER,
        amount REAL,
        transaction_date TEXT,
        exchange_type TEXT,
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (currency_id) REFERENCES currency(currency_id)
    )
    """)

    conn.commit()
    conn.close()
    print("All tables created successfully.")