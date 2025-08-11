def main():
    print("Welcome to the Canadian Dollar Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    canadian_dollar = convert_to_canadian_dollar(dollars)

    print("That's", canadian_dollar, "Canadian Dollars.")

convert_to_canadian_dollar = lambda dollars: dollars * 1.38
main()