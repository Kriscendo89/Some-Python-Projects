def main():
    print("Welcome to the Nigerian Naira Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    naira = convert_to_naira(dollars)

    print("That's", naira, "Nigerian Nairas.")

convert_to_naira = lambda dollars: dollars * 1534.56
main()