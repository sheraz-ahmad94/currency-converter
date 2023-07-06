import requests
import json

API_KEY = 'YOUR_API_KEY'
BASE_URL = "https://v6.exchangerate-api.com/v6"

def menu():
    print("-" * 20)
    print("Currency Converter")
    print("-" * 20)
    print("1. USD to EUR")
    print("2. USD to GBP")
    print("3. EUR to USD")
    print("4. EUR to GBP")
    print("5. GBP to USD")
    print("6. GBP to EUR")
    print("7. Quit")

def url_builder(currency):
    url = f"{BASE_URL}/{API_KEY}/latest/{currency}"
    return url

def convert(data, amount, to_currency):
    conversion = amount * data['conversion_rates'][to_currency]
    return conversion

response_usd = requests.get(url_builder("USD"))
response_eur = requests.get(url_builder("EUR"))
response_gbp = requests.get(url_builder("GBP"))

if response_usd.status_code == 200:
    data_usd = response_usd.json()
    data_eur = response_eur.json()
    data_gbp = response_gbp.json()
    
    while True:
        menu()
        option = int(input("Select an Option: "))

        if option == 1 or option == 2:
            amount = float(input("\nEnter Amount in USD: "))
            if option == 2:
                conversion = round(convert(data_usd, amount, 'GBP'), 3)
                print(f"\nConversion Result: \n{amount} USD = {conversion} GBP")
            else:
                conversion = round(convert(data_usd, amount, 'EUR'), 3)
                print(f"\nConversion Result: \n{amount} USD = {conversion} EUR")

        elif option == 3 or option == 4:
            amount = float(input("\nEnter Amount in EUR: "))

            if option == 4:
                conversion = round(convert(data_eur, amount, 'GBP'), 3)
                print(f"\nConversion Result: \n{amount} EUR = {conversion} GPB")
            else:
                conversion = round(convert(data_eur, amount, 'USD'), 3)
                print(f"\nConversion Result: \n{amount} EUR = {conversion} USD")

        elif option == 5 or option == 6:
            amount = float(input("Enter Amount in GBP: "))

            if option == 6:
                conversion = round(convert(data_gbp, amount, 'EUR'), 3)
                print(f"\nConversion Result: \n{amount} GBP = {conversion} EUR")
            else:
                conversion = round(convert(data_gbp, amount, 'USD'), 3)
                print(f"\nConversion Result: \n{amount} GBP = {conversion} USD")
            
        elif option == 7:
            break
        else:
            print("Wrong Option")
        




