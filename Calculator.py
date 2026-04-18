# Function 1: Addition
def add(a, b):
    return a + b

# Function 2: Multiplication
def multiply(a, b):
    return a * b

# Function 3: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Choose operation:")
    print("1. Add")
    print("2. Multiply")
    print("3. Factorial")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == '2':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == '3':
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    else:
        print("Invalid choice")

main()