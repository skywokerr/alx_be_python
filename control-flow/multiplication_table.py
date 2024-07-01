# multiplication_table.py

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Prompt the user to enter a number
number = get_number("Enter a number to see its multiplication table: ")

# Generate and print the multiplication table from 1 to 10
for i in range(1, 10 + 1):
    product = number * i
    print(f"{number} * {i} = {product}")
