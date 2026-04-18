def calculate_power(x, y):
    return x ** y

def main():
    print("Power Calculator (x^y)")
    
    try:
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))
        
        result = calculate_power(x, y)
        print(f"\nResult: {x}^{y} = {result}")
    
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
