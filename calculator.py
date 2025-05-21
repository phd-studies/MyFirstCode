def calculator():
    """A simple command-line calculator."""
    print("Simple Calculator")
    print("-----------------")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye! 👋")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers. 🔢")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero. 🚫")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid input. Please select a valid option. 🤔")

if __name__ == "__main__":
    calculator()
