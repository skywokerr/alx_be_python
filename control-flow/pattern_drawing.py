# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the square pattern using nested loops
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing a row
    row += 1
