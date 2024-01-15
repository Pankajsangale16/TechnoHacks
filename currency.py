from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()

    print("Welcome to the Currency Converter!")

    from_currency = input("Enter the currency code you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency code you want to convert to (e.g., EUR): ").upper()

    try:
        amount = float(input("Enter the amount you want to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
    except:
        print(f"Unable to fetch exchange rate for {from_currency} to {to_currency}. Please check your currency codes.")
        return

    converted_amount = amount * exchange_rate

    print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
