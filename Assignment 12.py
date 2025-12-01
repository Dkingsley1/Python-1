rows = int(input("Enter the number of rows:"))
char = input("Enter the character to use:")

print()

for i in range(1, rows + 1):
    print(char * i)