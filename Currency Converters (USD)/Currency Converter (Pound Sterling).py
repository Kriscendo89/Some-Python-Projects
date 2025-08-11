def main():
    print("Welcome to the Pound Sterling Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    pound = convert_to_pound(dollars)

    print("That's", pound, "Pounds.")

convert_to_pound = lambda dollars: dollars * 0.74

main()