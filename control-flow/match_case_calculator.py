# match_case_calculator.py

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompt the user to enter two numbers
num1 = int(get_number("Enter the first number: "))
num2 = int(get_number("Enter the second number: "))

# Prompt the user to select an operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation selected."

# Output the result
print(f"The result is: {result}")
