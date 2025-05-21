def calculator():
    """A simple command-line calculator."""

    # Theme selection
    print("Select a theme:")
    print("1. Light")
    print("2. Dark")
    theme_choice = input("Enter choice (1/2) or press Enter for dark theme: ")

    if theme_choice == '1':
        # Light theme: black text on white background
        FG_COLOR = "\033[30m"
        BG_COLOR = "\033[47m"
        THEME_NAME = "light"
        print("Light theme selected.")
    elif theme_choice == '2' or not theme_choice:
        # Dark theme: white text on black background (default)
        FG_COLOR = "\033[97m"  # Bright white
        BG_COLOR = "\033[40m"  # Black
        THEME_NAME = "dark"
        if not theme_choice:
            print("Defaulting to dark theme.")
        else:
            print("Dark theme selected.")
    else:
        print("Invalid theme choice. Defaulting to dark theme.")
        FG_COLOR = "\033[97m"
        BG_COLOR = "\033[40m"
        THEME_NAME = "dark"

    # Reset colors at the end
    RESET_COLOR = "\033[0m"

    # Apply theme to the calculator interface
    print(f"{BG_COLOR}{FG_COLOR}")
    print("Simple Calculator")
    print("-----------------")
    print(RESET_COLOR) # Reset after header

    while True:
        print(f"{RESET_COLOR}{BG_COLOR}{FG_COLOR}\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input(f"Enter choice (1/2/3/4/5): {RESET_COLOR}") # Reset after input

        if choice == '5':
            print(f"{BG_COLOR}{FG_COLOR}Exiting calculator. Goodbye! 👋{RESET_COLOR}")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1_input = input(f"{BG_COLOR}{FG_COLOR}Enter first number: {RESET_COLOR}")
                num2_input = input(f"{BG_COLOR}{FG_COLOR}Enter second number: {RESET_COLOR}")
                num1 = float(num1_input)
                num2 = float(num2_input)
            except ValueError:
                print(f"{BG_COLOR}{FG_COLOR}Invalid input. Please enter numbers. 🔢{RESET_COLOR}")
                continue

            # Perform calculation and display result with theme colors
            result_prefix = f"{BG_COLOR}{FG_COLOR}"
            result_suffix = f"{RESET_COLOR}"

            if choice == '1':
                print(f"{result_prefix}{num1} + {num2} = {num1 + num2}{result_suffix}")
            elif choice == '2':
                print(f"{result_prefix}{num1} - {num2} = {num1 - num2}{result_suffix}")
            elif choice == '3':
                print(f"{result_prefix}{num1} * {num2} = {num1 * num2}{result_suffix}")
            elif choice == '4':
                if num2 == 0:
                    print(f"{result_prefix}Error! Division by zero. 🚫{result_suffix}")
                else:
                    print(f"{result_prefix}{num1} / {num2} = {num1 / num2}{result_suffix}")
        else:
            print(f"{BG_COLOR}{FG_COLOR}Invalid input. Please select a valid option. 🤔{RESET_COLOR}")

if __name__ == "__main__":
    try:
        calculator()
    except KeyboardInterrupt:
        # Reset colors if the program is interrupted (e.g., Ctrl+C)
        print("\033[0m")
        print("Calculator exited.")
