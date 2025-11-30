# Leap year checker with Error Handling

year_input = input("Enter a year: ")

# Validate numeric input
if not year_input.isdigit():
    print("Error: Please enter a calid numeric year.")
else:
    year = int(year_input)

    # Leap year logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not leap year")