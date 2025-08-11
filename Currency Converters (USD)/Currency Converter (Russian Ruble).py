def main():
    print("Welcome to the Russian Ruble Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    ruble = convert_to_ruble(dollars)

    print("That's", ruble, "Russian Rubles.")

convert_to_ruble = lambda dollars: dollars * 79.50
main()