

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"


def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def display_results(calc):
    print("\nResults:")
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())


def main():
    a, b = get_input()
    calc = Calculator(a, b)
    display_results(calc)


if __name__ == "__main__":
    main()