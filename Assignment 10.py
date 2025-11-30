# Ask the user to enter their age
age_input = input("Enter your age: ")

# check if the input is the number and not an empty string
if age_input.isdigit():
    age=int(age_input)

    if age > 0:
        # check the classifications
            if age < 18:
                print("Minor")
            elif 18 <= age <= 65:
                print("Adult")
            else:
                print("Senior Citizen")
    else:
        print("error")

