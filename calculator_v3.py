def calculator():
    import operator

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    while True:
        print("\n===== Terminal Calculator =====")
        op = input("Enter an operator (+, -, *, /) or q to quit: ").strip()

        if op.lower() == "q":
            print("Goodbye!")
            break

        if op not in operations:
            print("Invalid operator! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == "/" and num2 == 0:
                print("Cannot divide by zero!")
                continue

            total = operations[op](num1, num2)
            print(f"Total = {total}")

        except ValueError:
            print("Invalid number! Please enter a valid number.")
        except Exception as e:
            print(f"Something went wrong! {e}")

calculator()