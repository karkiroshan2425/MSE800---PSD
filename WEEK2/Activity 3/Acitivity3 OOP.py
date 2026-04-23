class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def factorial(self, n):
        if n < 0:
            return "Factorial not defined for negative numbers"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def get_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b


def show_menu():
    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Factorial")


def main():
    calc = Calculator()

    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice in ["1", "2", "3"]:
        a, b = get_two_numbers()
        calc = Calculator(a, b)

        if choice == "1":
            print("Result:", calc.add())
        elif choice == "2":
            print("Result:", calc.subtract())
        elif choice == "3":
            print("Result:", calc.multiply())

    elif choice == "4":
        num = int(input("Enter a number for factorial: "))
        print("Factorial:", calc.factorial(num))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()