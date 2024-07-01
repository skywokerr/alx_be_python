# pattern_drawing.py

def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Prompt the user to enter a positive integer
size = get_positive_integer("Enter the size of the pattern: ")

# Draw the square pattern using nested loops
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing a row
    row += 1
