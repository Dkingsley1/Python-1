# Grade Calculator with Validation

marks = []

for i in range(3):
    value = input(f"Enter mark for subject {i+1} (0-100): ")

    # Validate numeric
    if not value.isdigit():
        print("Error: Marks must be between 0 and 100.")
        exit()

    value = int(value)

    # Validate range
    if value < 0 or value > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()
    marks.append(value)

avg = sum(marks) / 3

# Determine grade
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade ="C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Average: {avg:.2f}")
print("Grade:", grade)