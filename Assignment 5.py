def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a numeric value.")
# Input
hours = get_non_negative_number("Enter a time duration in hours: ")

# Processing
minutes = hours * 60
seconds = hours * 3600

# Output
print(f"\nTime Duration:")
print(f"Minutes: {minutes:.2f}")
print(f"Seconds: {seconds:.2f}")