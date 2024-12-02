import requests

# Function to fetch exchange rates and convert currency
def currency_converter(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        rates = response.json()["rates"]
        if to_currency in rates:
            converted_amount = amount * rates[to_currency]
            return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            return "Invalid target currency."
    else:
        return "Failed to fetch exchange rates."

# Main program
print("Welcome to the Currency Converter!")
while True:
    from_currency = input("\nEnter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
        print(currency_converter(amount, from_currency, to_currency))
    except ValueError:
        print("Invalid amount. Please enter a number.")
    
    again = input("Would you like to convert another amount? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
