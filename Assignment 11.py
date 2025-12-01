while True:
    user_input = input("Enter a positive integer: ")

    # Validate numeric input
    if not user_input.isdigit():
        print("Error: Please enter a calid positive number.\n")
        continue

    n = int(user_input)
    if n <= 0:
        print("Error: Number must be positive.\n")
        continue

    break
print("\nCollatz sequence:")
print(n,end=" ")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(n, end=" ")
print("\nDone!")
