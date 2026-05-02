
import sqlite3

DB_NAME = "money_exchange.db"


def connect():
    return sqlite3.connect(DB_NAME)



def add_customer(full_name, email, phone_number, address):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO customer (full_name, email, phone_number, address)
    VALUES (?, ?, ?, ?)
    """, (full_name, email, phone_number, address))

    conn.commit()
    conn.close()
    print("Customer added successfully.")


def view_customers():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()

    conn.close()
    return data


def search_customer(name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM customer
    WHERE full_name LIKE ?
    """, ('%' + name + '%',))

    data = cursor.fetchall()

    conn.close()
    return data


def delete_customer(customer_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM customer
    WHERE customer_id = ?
    """, (customer_id,))

    conn.commit()
    conn.close()
    print("Customer deleted successfully.")

def view_currencies():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM currency")
    data = cursor.fetchall()

    conn.close()
    return data

def view_transactions():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        transactions.transaction_id,
        customer.full_name,
        currency.currency_name,
        transactions.amount,
        transactions.transaction_date,
        transactions.exchange_type
    FROM transactions
    LEFT JOIN customer
        ON transactions.customer_id = customer.customer_id
    LEFT JOIN currency
        ON transactions.currency_id = currency.currency_id
    """)

    data = cursor.fetchall()

    conn.close()
    return data

