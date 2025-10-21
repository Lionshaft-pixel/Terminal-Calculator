operator = input("Enter an operator (+, -, *, /): ")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if operator == "+":
    total = first_number + second_number
elif operator == "-":
    total = first_number - second_number
elif operator == "*":
    total = first_number * second_number
elif operator == "/":
    total = first_number / second_number

print(total)