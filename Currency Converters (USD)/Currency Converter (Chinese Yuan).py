def main():
    print("Welcome to the Chinese Yuan Currency Converter!")
    print()

    dollars = eval(input("Enter the amount in US Dollars:"))

    yuan = convert_to_yuan(dollars)

    print("That's", yuan, "Chinese Yuan.")

convert_to_yuan = lambda dollars: dollars * 7.19

main()