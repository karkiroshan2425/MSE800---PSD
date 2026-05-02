
from database import create_tables
from user_manager import (
    add_customer,
    view_customers,
    search_customer,
    delete_customer,
    view_currencies,
    view_transactions
)


def menu():
    print("\n====== MONEY EXCHANGE SYSTEM ======")
    print("1. Add Customer")
    print("2. View All Customers")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. View Currencies")
    print("6. View Transactions")
    print("7. Exit")


def main():
    create_tables()

    while True:
        menu()
        choice = input("Select an option (1-7): ")

        if choice == '1':
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")

            add_customer(full_name, email, phone, address)

        elif choice == '2':
            customers = view_customers()
            for customer in customers:
                print(customer)

        elif choice == '3':
            name = input("Enter customer name to search: ")
            customers = search_customer(name)
            for customer in customers:
                print(customer)

        elif choice == '4':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)

        elif choice == '5':
            currencies = view_currencies()
            for currency in currencies:
                print(currency)

        elif choice == '6':
            transactions = view_transactions()
            for transaction in transactions:
                print(transaction)

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
