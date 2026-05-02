from rectangle import Rectangle

def main():
    print("=== Area and Perimeter Calculator ===")

    length = float(input("Enter the length of the land: "))
    width = float(input("Enter the width of the land: "))

    land = Rectangle(length, width)

    area = land.calculate_area()
    perimeter = land.calculate_perimeter()

    print("\nResults:")
    print(f"Area of the land: {area}")
    print(f"Perimeter of the land: {perimeter}")

if __name__ == "__main__":
    main()