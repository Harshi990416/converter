def currency_converter():
    # Hardcoded exchange rates relative to USD
    rates = {
        "USD": 1.0,
        "INR": 82.50,
        "EUR": 0.91,
        "GBP": 0.78,
        "JPY": 146.5,
        "AUD": 1.52,
        "CAD": 1.34,
    }

    print("Available currencies:", ", ".join(rates.keys()))

    while True:
        from_currency = input("From currency (e.g., USD): ").upper()
        if from_currency in rates:
            break
        print("Currency not supported. Please enter again.")

    while True:
        to_currency = input("To currency (e.g., EUR): ").upper()
        if to_currency in rates:
            break
        print("Currency not supported. Please enter again.")

    while True:
        try:
            amount = float(input(f"Amount in {from_currency}: "))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    # Convert from source to USD, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]

    print(f"\n{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()