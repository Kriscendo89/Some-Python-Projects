def main():
    print("Welcome to the Euro Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    euro = convert_to_euro(dollars)

    print("That's", euro, "Euros.")

convert_to_euro = lambda dollars: dollars * 0.86
main()