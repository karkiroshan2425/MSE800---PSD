This project is developed using Python and SQLite3 based on the ER Diagram for a Finance Money Exchange Software Application.

CUSTOMER TABLE:
Stores customer details for users who perform money exchange transactions.
Every transaction must belong to a customer.

ATTRIBUTES:
- customer_id (PK)
- full_name
- email
- phone_number
- address

EMPLYOEE TABLE:
Stores employee details for staff managing exchange transactions.
Each transaction must be handled by an employee for tracking and accountability.

ATTRIBUTES:
- employee_id (PK)
- full_name
- position
- email
- phone_number

CURRENCY TABLE:
Stores available foreign currencies.
Customers exchange money using different currencies such as USD, EUR, GBP, etc.

ATTRIBUTES:
- currency_id (PK)
- currency_name
- currency_code
- country
- symbol

EXCHANGE RATE TABLE:
Stores buying and selling rates for each currency.
Rates change frequently and need separate management.

ATTRIBUTES:
- rate_id (PK)
- currency_id (FK)
- buying_rate
- selling_rate
- updated_date
- status

TRANSACTIONS TABLE:
Stores all exchange transactions.
This is the main table connecting customer, employee, and currency.

ATTRIBUTES:
- transaction_id (PK)
- customer_id (FK)
- employee_id (FK)
- currency_id (FK)
- amount
- transaction_date
- exchange_type


PROJECT FILES:
- main.py
- database.py
- user_manager.py
- README.md
- money_exchange.db

