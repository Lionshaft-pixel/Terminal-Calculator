while True:
    try:
        print("\n===== Terminal Calculator =====")
        operator = input("Enter an operator (+, -, *, / or q to quit): ")
        if operator.lower() == "q":
            print("Goodbye!")
            break

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if operator == "+":
            total = first_number + second_number
        elif operator == "-":
            total = first_number - second_number
        elif operator == "*":
            total = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                total = "You cannot divide a number by 0!"
            else:
                total = first_number / second_number
        else:
            total = "Please enter a valid operator!"

        print(f"Total = {total}")

    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Something went wrong! Please try again later! {e}")