import math
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a numeric value.")

# Input
print("Enter the coordinates of the first point:")
x1 = get_number("x1: ")
y1 = get_number("y1: ")

print("\nEnter the coordinates of the second point:")
x2 = get_number ("x2: ")
y2 = get_number ("y2: ")

# Processing
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print(f"\nThe distance between the two points is: {distance:.4f}")
