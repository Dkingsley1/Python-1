def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Amount cannot be negative.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a numeric value.")
# Fixed exchange rates (example)
exchange_rates = {
    "USD to EUR": 0.92,
    "USD to GBP": 0.78,
    "USD to JPY": 153.40,
    "USD to CAD": 1.37
}

# Display currency options
print("Available currency pairs:")
for pair in exchange_rates:
    print(" -", pair)

# Get a calid currency pair
while True:
    choice = input("\nEnter a currency pair exactly as show (e.g., USD to EUR): ")
    if choice in exchange_rates:
        break
    else:
        print("Error: Invalid currency pair. Please choose from the list.")

# Get amount in USD
amount_usd = get_positive_number("\nEnter an amount in USD: ")

# Conversion
rate = exchange_rates[choice]
converted_amount = amount_usd * rate

# Output
print(f"\nConverted amount from {choice}: {converted_amount:.2f}")